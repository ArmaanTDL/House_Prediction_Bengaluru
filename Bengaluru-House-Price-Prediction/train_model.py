import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('data.csv')

# Drop unnecessary columns
df2 = df.drop(['availability', 'society'], axis='columns')

# Handle missing values
df3 = df2.dropna()

# Clean 'size' column to get 'bhk'
df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))

# Clean 'total_sqft'
def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None

df4 = df3.copy()
df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_to_num)
df4 = df4.dropna()

# Handle locations - keep top 100 or so to keep it simple, others as 'other'
df5 = df4.copy()
df5.location = df5.location.apply(lambda x: x.strip())
location_stats = df5.groupby('location')['location'].count().sort_values(ascending=False)
location_stats_less_than_10 = location_stats[location_stats <= 10]
df5.location = df5.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)

# One hot encoding for location and area_type
def build_model(df):
    dummies_loc = pd.get_dummies(df.location)
    dummies_area = pd.get_dummies(df.area_type)
    df6 = pd.concat([df, dummies_loc, dummies_area], axis='columns')
    df7 = df6.drop(['location', 'size', 'area_type', 'other'], axis='columns') 

    X = df7.drop('price', axis='columns')
    y = df7.price

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

    lr_clf = LinearRegression()
    lr_clf.fit(X_train, y_train)
    
    # Save column names to help with prediction later
    columns = {
        'data_columns' : [col.lower() for col in X.columns]
    }
    with open("columns.json", "w") as f:
        import json
        f.write(json.dumps(columns))
        
    # Save location names for dropdown
    locations = sorted(df.location.unique().tolist())
    area_types = sorted(df.area_type.unique().tolist())
    with open("metadata.pkl", "wb") as f:
        pickle.dump({'locations': locations, 'area_types': area_types}, f)

    return lr_clf

model = build_model(df5)

# Save the model
with open('bengaluru_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model and metadata saved successfully.")

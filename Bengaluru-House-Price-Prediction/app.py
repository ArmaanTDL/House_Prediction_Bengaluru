from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np
import os

app = Flask(__name__)

# Constants
MODEL_PATH = "bengaluru_model.pkl"
COLUMNS_PATH = "columns.json"
METADATA_PATH = "metadata.pkl"

# Global variables
__locations = None
__area_types = None
__data_columns = None
__model = None

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __area_types
    global __model

    # Use absolute paths if needed, but here we assume relative to this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(current_dir, COLUMNS_PATH), "r") as f:
        __data_columns = json.load(f)['data_columns']
        
    with open(os.path.join(current_dir, METADATA_PATH), "rb") as f:
        meta = pickle.load(f)
        __locations = meta['locations']
        __area_types = meta['area_types']

    with open(os.path.join(current_dir, MODEL_PATH), 'rb') as f:
        __model = pickle.load(f)
    print("Artifacts loaded successfully.")

@app.route('/')
def home():
    if __locations is None:
        load_saved_artifacts()
    return render_template('index.html', locations=__locations, area_types=__area_types)

@app.route('/predict', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        area_type = request.form['area_type']

        # Get indices for dummies
        loc_index = -1
        if location.lower() in __data_columns:
            loc_index = __data_columns.index(location.lower())
            
        area_index = -1
        if area_type.lower() in __data_columns:
            area_index = __data_columns.index(area_type.lower())

        # Prepare input vector
        x = np.zeros(len(__data_columns))
        x[0] = total_sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1
        if area_index >= 0:
            x[area_index] = 1

        prediction = __model.predict([x])[0]
        prediction = round(float(prediction), 2)
        
        # Format the price
        price_str = f"₹{prediction} Lakhs"
        if prediction >= 100:
            price_str = f"₹{round(prediction/100, 2)} Crores"

        return jsonify({
            'success': True,
            'estimated_price': price_str,
            'details': {
                'Location': location,
                'BHK': bhk,
                'Bathrooms': bath,
                'Area Type': area_type,
                'Total Sqft': total_sqft
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == "__main__":
    load_saved_artifacts()
    # Using port 5002 to avoid conflict with the other House Prediction app if it's still running
    app.run(host='0.0.0.0', port=5002, debug=True)

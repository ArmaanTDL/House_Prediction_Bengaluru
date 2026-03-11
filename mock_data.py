import pandas as pd
import numpy as np
import os

os.makedirs('data', exist_ok=True)

# Define column names from rename_columns
cols = [
    'parcelid', 'airconditioningtypeid', 'architecturalstyletypeid', 'basementsqft',
    'bathroomcnt', 'bedroomcnt', 'buildingclasstypeid', 'buildingqualitytypeid',
    'calculatedbathnbr', 'decktypeid', 'finishedfloor1squarefeet',
    'calculatedfinishedsquarefeet', 'finishedsquarefeet12', 'finishedsquarefeet13',
    'finishedsquarefeet15', 'finishedsquarefeet50', 'finishedsquarefeet6',
    'fips', 'fireplacecnt', 'fullbathcnt', 'garagecarcnt', 'garagetotalsqft',
    'hashottuborspa', 'heatingorsystemtypeid', 'latitude', 'longitude',
    'lotsizesquarefeet', 'poolcnt', 'poolsizesum', 'pooltypeid10',
    'pooltypeid2', 'pooltypeid7', 'propertycountylandusecode',
    'propertylandusetypeid', 'propertyzoningdesc', 'rawcensustractandblock',
    'regionidcity', 'regionidcounty', 'regionidneighborhood', 'regionidzip',
    'roomcnt', 'storytypeid', 'threequarterbathnbr', 'typeconstructiontypeid',
    'unitcnt', 'yardbuildingsqft17', 'yardbuildingsqft26', 'yearbuilt',
    'numberofstories', 'fireplaceflag', 'structuretaxvaluedollarcnt',
    'taxvaluedollarcnt', 'assessmentyear', 'landtaxvaluedollarcnt',
    'taxamount', 'taxdelinquencyflag', 'taxdelinquencyyear', 'censustractandblock'
]

def generate_properties(filename):
    df = pd.DataFrame(np.random.randn(100, len(cols)), columns=cols)
    df['parcelid'] = range(100)
    df['propertycountylandusecode'] = '0100'
    df['propertyzoningdesc'] = 'LARS'
    df['hashottuborspa'] = 'Y'
    df['fireplaceflag'] = 'true'
    df['taxdelinquencyflag'] = 'Y'
    df.to_csv(filename, index=False)

def generate_train(filename):
    df = pd.DataFrame({
        'parcelid': range(100),
        'logerror': np.random.randn(100),
        'transactiondate': ['2016-01-01'] * 100
    })
    df.to_csv(filename, index=False)

generate_properties('data/properties_2016.csv')
generate_properties('data/properties_2017.csv')
generate_train('data/train_2016_v2.csv')
generate_train('data/train_2017.csv')

print("Mock data generated successfully.")

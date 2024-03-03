import xml.etree.ElementTree as ET
import datetime as dt
import pandas as pd

data_path = './exports/export.xml'

# Parse Tree
tree = ET.parse( data_path )
root = tree.getroot()
record_list = [x.attrib for x in root.iter('Record')]

# Parse XML to Dataframe
df = pd.DataFrame(record_list)

# Clean up some stuff.
for col in ['creationDate', 'startDate', 'endDate']:
    df[col] = pd.to_datetime(df[col])

df['value'] = pd.to_numeric(df['value'], errors='coerce')
df['value'] = df['value'].fillna(1.0)

df['type'] = df['type'].str.replace('HKQuantityTypeIdentifier', '')
df['type'] = df['type'].str.replace('HKCategoryTypeIdentifier', '')


df = df.drop(['sourceVersion'], axis=1)


# Extract to local directory
extract_cleaned_df = df.to_csv('data.csv', index=False)






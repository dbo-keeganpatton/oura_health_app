import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# Data and ease of view. 
pd.set_option('display.max_columns', 500 )
df = pd.read_csv('data.csv')

# I only care about these metrics for the type of measures.
# Device is a column that is all Null, remove as well.
type_column_values_to_keep = [ 
 'BodyMass', 'HeartRate', 'RespiratoryRate',
 'StepCount', 'DistanceWalkingRunning', 'WalkingSpeed', 
 'BasalEnergyBurned', 'ActiveEnergyBurned', 'FlightsClimbed', 
 'SleepAnalysis'
 ]

df.drop(['device'], axis=1, inplace=True)
df = df[df['type'].isin(type_column_values_to_keep)] 

# Split data between ring and phone
oura_df = df[df['sourceName'] == 'Oura']
iphone_df = df[df['sourceName'] == 'iPhone'] 

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

df = df[df['type'].isin(type_column_values_to_keep)] 
df.drop(['device'], axis=1, inplace=True)


print(df.head())

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', 500 )
pd.set_option('display.max_rows', 500 )


############################################
"""               Stage                  """
############################################

df = pd.read_csv('data.csv').query(
        "sourceName == 'Oura' & type == 'HeartRate'" 
).drop(
        ['device', 'creationDate'], axis=1
).assign(
        eventDate = lambda x: pd.to_datetime(x['startDate']).dt.date,
        eventYear = lambda x: pd.to_datetime(x['startDate']).dt.year,
        eventWkNm = lambda x: pd.to_datetime(x['startDate']).dt.isocalendar().week,
        eventWkYr = lambda x: x['eventYear'].astype(str) + "-" + x['eventWkNm'].astype(str) )


############################################
"""               Trend Agg              """ 
############################################

daily_trend_df = df.groupby(['eventWkYr']).mean(['value']).round().reset_index()

# Plot
x = daily_trend_df['eventWkYr']
y = daily_trend_df['value']

fig, ax = plt.subplots(figsize=(15,10), facecolor=('#161A1D'))
plt.title("Average Weekly Heart Rate", fontsize=18, color='white', pad=15)

# Overly Arduos Axis style config
ax.plot(x, y, linewidth=4.0, color='#C9372C')
ax.set_facecolor('#161A1D')
ax.spines["bottom"].set_color("white")     
ax.spines["top"].set_color("white")
ax.spines["left"].set_color("white")   
ax.spines['right'].set_color('white')

plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
ax.tick_params(axis='x', colors='white', which='both', size=12)
ax.tick_params(axis='y', colors='white', which='both', size=12)
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')


plt.savefig('./plot_images/wow_bpm.png')
# plt.savefig('/mnt/c/Users/Keegan/OneDrive/Desktop/images/health_data_figs/test.png')


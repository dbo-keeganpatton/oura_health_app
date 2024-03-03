import pandas as pd
import datetime as dt
import numpy as np
import streamlit as st
import altair as alt 


st.set_page_config(layout='wide')
############################################
###               Stage                  ###
############################################

heart_df = pd.read_csv('data.csv').query(
        "sourceName == 'Oura' & type == 'HeartRate'" 
).drop(
        ['device', 'creationDate'], axis=1
).assign(
        eventDate = lambda x: pd.to_datetime(x['startDate']).dt.date,
        eventYear = lambda x: pd.to_datetime(x['startDate']).dt.year,
        eventWkNm = lambda x: pd.to_datetime(x['startDate']).dt.isocalendar().week,
        eventWkYr = lambda x: x['eventYear'].astype(str) + "-" + x['eventWkNm'].astype(str) )


#################
##    Viz     ###
#################

# Heart Line Chart
weekly_bpm_line = heart_df.groupby(['eventWkYr']).mean('value').round().reset_index()

line = alt.Chart( 
    weekly_bpm_line, 
    title="Avg Heart Rate Weekly" ).mark_line(color="#C9372C").encode(
    x=alt.X('eventWkYr', title="", axis=alt.Axis(labelAngle= -45)),
    y=alt.Y('value', title="", scale=alt.Scale(domain=[50,60])),
    strokeWidth=alt.value(6)
).properties(width=1350, height=400)

text = line.mark_text(
    align='left',
    baseline='middle',
    fontSize=32,
    color='#FFFFFF',
    dx=7
).encode(text='value')

line_chart = alt.layer(
    line,
    text
).configure_axis(
    labelFontSize=20
).configure_title(
    fontSize=24,
    anchor='middle'
).properties(width=1350, height=400)


##############################################
###                 App                    ###
##############################################

def app():
    '''app body'''

    st.altair_chart(line_chart)

app()



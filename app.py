import pandas as pd
import datetime as dt
import numpy as np
import streamlit as st
import altair as alt 


st.set_page_config(layout='wide')
############################################
"""               Stage                  """
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
"""    Viz    """
#################

weekly_bpm_line = heart_df.groupby(['eventWkYr']).mean('value').round().reset_index()

line_chart = alt.Chart( 
    weekly_bpm_line, 
    title="Avg Heart Rate Weekly"
).mark_line().encode(
    x=alt.X('eventWkYr'),
    y=alt.Y('value')
)


##############################################
"""                 App                    """
##############################################

def app():
    '''app body'''

    st.altair_chart(line_chart)

app()



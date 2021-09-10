import streamlit as st
import numpy as np
import pandas as pd

st.title('Uber pickups in NYC')

date_column = 'date/time'
data_url = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache

def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x : str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column] = pd.to_datetime(data[date_column])
    return data

data_load_state = st.text('Loading data....')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)") 

if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[date_column].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider('hour',0,23,17)
filtered_data = data[data[date_column].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00'%hour_to_filter)
st.map(filtered_data)
import streamlit as st 
import time 

@st.cache_data  # Cache this data for 60 seconds , for mutable datas only 
def fetch_data():
    # Simulate  a slow data-fetching process 
    time.sleep(3) # Delays to mimic an API call
    return {"data": "This is cached data"}

st.write("Fetching data...")
data=fetch_data()
st.write(data)
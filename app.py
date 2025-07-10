import pickle
import pandas as pd
import numpy as np
import streamlit as st

st.title('Bengaluru House Price Detector system')
with open('pipeline.pkl', 'rb') as f:
    loaded_pipe = pickle.load(f)
def predict_price(new_data: pd.DataFrame):
    """
    Predict house prices given a DataFrame `new_data` with the same columns as the training data.
    """
    return loaded_pipe.predict(new_data)
data = pd.read_csv('cleandata.csv')
location = st.selectbox(
    "Select location from given locations in Bengaluru",
    data['location'].unique(),
)
bhk = st.number_input("Type bhk", value=2, min_value=1, max_value=16)
total_sqft = st.number_input("Type sqft", value=1000, min_value=300, max_value = 700000)
bath = st.number_input("Type no of bathrooms", value=2, min_value=1, max_value = 16)
availability = st.selectbox("Select if the house is ready to move in", ['Yes it is', 'No it is yet to be ready'])
if availability=='Yes it is':
    availability= 1
else:
    availability = 0

df = pd.DataFrame([{
    'availability': availability,
    'location': location,
    'bhk': bhk,
    'total_sqft': total_sqft,
    'bath': bath,
    'total_sqftbybhk': total_sqft/bhk
}])
if st.button("Predict price"):
    try:
        x = loaded_pipe.predict(df)
        st.write("Price is Rs.", int(x[0]*100000))
    except:
        st.write('error has occured')


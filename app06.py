# Tables and Dataframes:
import streamlit as st

import pandas as pd 

data = {
    "Name":['Alice','Bob','Charlie'],
    "Age": [25,30,35],
    "City": ['New York','London','Paris']
}

#Approach 01
df = pd.DataFrame(data)

st.write("Using st.write for dataframe.")
st.write(df)

# Approach 02
st.write("Static_Table")
st.table(df)

#Approach 03

st.write("Interactive DataFrame")
st.dataframe(df)


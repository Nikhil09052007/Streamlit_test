import streamlit as st

# Date
date = st.date_input("enter a date: ")
st.write('Selected date:', date)

# Time
time = st.time_input("enter the time: ")
st.write('Entered Time: ',time)




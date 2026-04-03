import streamlit as st 
import pandas as pd 

person = {
    "name":"Alice",
    "age" : 25,
    "Skills": ["Python","Sreamlit","Data Science"]

}
st.json(person)
st.write("Dictionary displayed with st.write(): ",person)



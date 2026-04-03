# More features:

import streamlit as st 

#Slider
age = st.slider("select your age:", 0,15,25,50)
st.write("Age:",age)

# Number Box
number = st.number_input("Enter the value",min_value=0,max_value=100,value=10)
st.write("Number: ",number)

#Textbox
name = st.text_input("Enter your Name: ")
st.write("Hello",name)

#Area_TextBox
bio = st.text_area("Write a short bio: ")
st.write("Your bio: ",bio)
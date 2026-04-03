# Let's see some more features of streamlit.
import streamlit as st

if st.button("CLick Me"):
    st.write("Button Clicked!")

choice = st.radio("Choose an option:",["Mirchi","RedFM","Bajaao"])

st.write("You selected: ",choice)

agree = st.checkbox("I agreee")

if agree:
    st.write("Thanks for your concent!.")



# SelectBox:
genre = st.selectbox("Pick a genre:",["Science Fiction","Horror","Animation","Action","Drama","Romance"])

st.write("Your genre is:",genre)

# Multiselect:
subgenre = st.multiselect("Pick subgenre:",["Extreme","Light","Half","Full",'Noodles'])
st.write("Your subgenre: ",subgenre)


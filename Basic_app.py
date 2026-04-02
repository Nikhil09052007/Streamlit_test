# before initialising the basic syntax or the program we generally make an app.py as our remote opertator to our dashboard.

# To run this app.py or file name as extension of .py in localserver:= Hit "python -m streamlit run app.py" in terminal.
# Make sure to keep the terminal activate while performing the file.

import streamlit as st 

st.header("Let's see!") # header for the application.

st.title("Re-execution Do") # Title for the appliaction.
 # this works in real-time.


# Following are the ways for representation of the various aspects similar to python.
# for print in python use st.write("Message")


name = st.text_input("Enter your Name: ")

if name:
    st.write(f"Hello,{name}")
else:
    st.write("Please! Enter your Name.")

print("Script Executed") # This print will only work in terminal.


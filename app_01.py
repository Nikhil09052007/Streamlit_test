import streamlit as st 

st.title("This is the title.")
st.header("This is header")
st.subheader("This is subheader")


st.markdown("**MarkDown**")
st.text("This is plain text")
st.write("st.write can handle mixed characters and bold contexts and numbers.")



st.markdown('### Code Block Example')
st.code('''
Python Example:
def New(name):
    print(f"Hello! new member{name}")




''')
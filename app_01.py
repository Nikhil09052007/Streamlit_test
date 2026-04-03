import streamlit as st 

# Basic syntax used in streamlit to perform the representation of the frontened.


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
print(New("Streamlit")
''', language="python")

st.markdown("### Inline Latex: $a^2 + b^2 = c^2$ ")


st.success("This is a success message.")

st.warning("Be careful! This is a warning message.")

st.error("Something went wrong!, This rerpresents error..")

st.info("This is an info messagese.")

st.markdown("> **Tip:** Use feedback to guide the user.")



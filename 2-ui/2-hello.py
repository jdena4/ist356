import streamlit as st

st.title("Saying Hello!!!")
name = st.text_input("And you are?")
age = st.slider("How old are you?", 0, 130, 25)
mybutton = st.button("Activate")

if mybutton:
    st.write(f"Hello, {name}! You are {age} years old.")
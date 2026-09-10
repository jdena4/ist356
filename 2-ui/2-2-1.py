import streamlit as st

st.title("Area & Perimeter Calculator")

# Input fields for length and width
length = st.number_input("Enter the length of the rectangle:", min_value=0.0, step= 0.1)
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, step= 0.1)

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the results
st.write(f"The area of the rectangle is: {area}")
st.write(f"The perimeter of the rectangle is: {perimeter}")

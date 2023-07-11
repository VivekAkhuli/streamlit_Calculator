import streamlit as st
import numpy as np

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def sine(x):
    return np.sin(x)

def cosine(x):
    return np.cos(x)

def tangent(x):
    return np.tan(x)


# Calculator title
st.title("Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Operation selection
operation = st.selectbox("Select operation:", ("Addition", "Subtraction", "Multiplication", "Division", "Sine", "Cosine", "Tangent"))

# Perform the selected operation
result = 0
if operation == "Addition":
    result = add(num1, num2)
elif operation == "Subtraction":
    result = subtract(num1, num2)
elif operation == "Multiplication":
    result = multiply(num1, num2)
elif operation == "Division":
    if num2 != 0:  # Avoid division by zero
        result = divide(num1, num2)
    else:
        st.error("Cannot divide by zero.")
elif operation == "Sine":
    result = sine(num1)
elif operation == "Cosine":
    result = cosine(num1)
elif operation == "Tangent":
    result = tangent(num1)

# Display the result
if result is not None:
    st.success("Result: {}".format(result))

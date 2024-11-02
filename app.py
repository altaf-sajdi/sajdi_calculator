import streamlit as st

def sajdi_calculator():
    st.title("Sajdi Calculator")
    st.write("Select an operation:")
    operation = st.selectbox("Operation", ("Add", "Subtract", "Multiply", "Divide"))

    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = "Error! Division by zero." if num2 == 0 else num1 / num2

    st.write("Result:", result)

sajdi_calculator()

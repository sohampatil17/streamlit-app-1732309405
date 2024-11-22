import streamlit as st
import numpy as np

# Cache the data
@st.cache_data
def calculate_result(num1, num2, operation):
    try:
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed"
        else:
            return "Error: Invalid operation"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main application
def main():
    st.title("Calculator App")

    # Input fields
    num1 = st.number_input("Enter the first number", min_value=-1000.0, max_value=1000.0)
    num2 = st.number_input("Enter the second number", min_value=-1000.0, max_value=1000.0)

    # Select operation
    operations = ['add', 'subtract', 'multiply', 'divide']
    operation = st.selectbox("Select an operation", options=operations)

    # Calculate result
    result = calculate_result(num1, num2, operation)

    # Display result
    st.write("Result:")
    st.write(result)

    # Display error message if division by zero occurs
    if isinstance(result, str) and "Error: Division by zero" in result:
        st.error("Error: Division by zero is not allowed")

if __name__ == "__main__":
    main()
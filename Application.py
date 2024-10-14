import streamlit as st

# Define the functions for the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Adding custom CSS for the button hover effect
def add_button_hover_style():
    st.markdown(
        """
        <style>
        div.stButton > button:hover {
            background-color: red;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Streamlit app
def calculator_app():
    st.title("Simple Calculator")

    # Apply the custom button hover style
    add_button_hover_style()

    # Selection box for operation
    operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
    num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

    # Button to calculate the result
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        st.write(f"The result of {operation} between {num1} and {num2} is: {result}")

# Call the Streamlit app
if __name__ == "__main__":
    calculator_app()

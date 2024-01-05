import streamlit as st

st.header("**CS50 Intro to Programming with Python Assignments**")
st.markdown("---")
st.write("These are some of the assignments I have completed as part of CS50 python course")

# week 1:

def main():
    st.subheader("Basic Calculator App")

    expression = st.text_input("Enter expression (e.g., 5 + 3): ")

    if expression:
        try:
            x, y, z = map(str, expression.split())
            x, z = float(x), float(z)

            result = calculator(x, y, z)

            st.success(f"Result: {result}")
        except ValueError:
            st.error("Error: Invalid input. Please enter a valid expression.")
    else:
        st.warning("Enter an expression to calculate.")

def calculator(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        if z != 0:
            return x / z
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error"

main()
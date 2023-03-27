import streamlit as st
import sympy as sp
from PIL import Image
def solve_limit(expr, x, a):
    try:
        expr = sp.sympify(expr)
        lim = sp.limit(expr, x, a)
        return lim
    except:
        return "Error: Invalid input!"
image = Image.open('limit.jpg')
st.image(image)
def main():
    st.title("PYTHON PROJECT")
    image = Image.open('limit.jpg')
    st.image(image)
    st.header("Limits of a Function:-")
    #image = Image.open('limit.jpg')
    #st.image(image)
    st.write("Enter a function and the limit point.")
    expr = st.text_input("Enter the function:", "")
    x = st.text_input("Enter the variable:", "")
    a = st.text_input("Enter the limit :", "")
    if st.button("solve Limit"):
        ans = solve_limit(expr, x, a)
        st.write(f"The limit of the function as {x} approaches {a} is : {ans}")
if __name__ == "__main__":
    main()
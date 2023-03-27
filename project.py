import streamlit as st
import sympy as sp
from PIL import Image
import pandas as pd
import plotly.express as px
st.markdown("<h1 style='text-align: center;' >PYTHON PROJECT </h1>",unsafe_allow_html=True)
x1 , x2 , x3 = st.columns([5,10,5])
with x2:

    image = Image.open('python.jpg')
    st.image(image)


#limits
def solve_limit(expr, x1, a):
    try:
        expr = sp.sympify(expr)
        lim = sp.limit(expr, x1, a)
        return lim
    except:
        return "Error: Invalid input!"

def mains():
    
    st.header("Limits of a Function:-")
    image = Image.open('lim.jpg')
    st.image(image)
    st.write("Enter a function and the limit point.")
    expr = st.text_input("Enter the function:")
    x1 ="x" #st.text_input("Enter the variable:")
    a = st.text_input("Enter the limit :")
    if st.button("solve Limit"):
        ans = solve_limit(expr, x1, a)
        st.write(f"The limit of the function as {x1} approaches {a} is : {ans}")
if __name__ == "__main__":
    mains()
#derivative


def derivative():
    fx = st.text_input("Enter a function: ","x ")

    try:
        f = sp.sympify(fx)
        f_prime = sp.diff(f)
        st.write("The derivative of", fx, "is", f_prime)

    except sp.SympifyError:

        st.error("Invalid input, please enter a valid mathematical expression.")

if __name__ == "__main__":
    st.title("Derivatives of only one variable")
    image = Image.open('derivative.jpg')
    st.image(image)
    derivative()


#integral

def solve_integral(exp, var,p,q ):
    try:
        exp = sp.sympify(exp)
        solve = sp.integrate(exp, (var,p,q))
        return solve
    except:
        return "Error: Invalid input!"


def main():
   
    st.title("Integration Solver")
    image = Image.open('integration.jpg')
    st.image(image)
    st.write("Enter an expression, a variable, and the integration limits.")

    
    exp = st.text_input("Enter the expression:", "")
    var = st.text_input("Enter the variable:", "")
    p = st.text_input("Enter the lower limit:", "")
    q = st.text_input("Enter the upper limit:", "")

   
    if st.button("Solve Integral"):
        solve = solve_integral(exp, var, p, q)
        st.write(f"The integral of {exp} with respect to {var} from {p} to {q} is: {solve}")

if __name__ == "__main__":
    main()


#3D GRAPH
st.image("https://www.vcssl.org/en-us/code/archive/0001/7300-graph-file-animator-3d/screen")
def get_data():
    x = st.text_input("Enter values for X separated by commas:")
    y = st.text_input("Enter values for Y separated by commas:")
    z = st.text_input("Enter values for Z separated by commas:")
    x = [str(i) for i in x.split(",")]
    y = [str(i) for i in y.split(",")]
    z = [str(i) for i in z.split(",")]
    data = {'X': x, 'Y': y, 'Z': z}
    df = pd.DataFrame(data)
    return df


def app():
    st.title("3D Graph")
    st.write("Enter values for X, Y, Z to create a 3D graph.")
    df = get_data()
    fig = px.scatter_3d(df, x='X', y='Y', z='Z')
    st.plotly_chart(fig)

if __name__ == '__main__':
    app()






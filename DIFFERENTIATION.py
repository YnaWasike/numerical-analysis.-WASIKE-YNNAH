import sympy as sp

# Define the symbolic variable and function
x = sp.symbols('x')
function = x**2 + 3*x + 2

# Differentiate the function
derivative = sp.diff(function, x)

print(f"Function: {function}")
print(f"Derivative: {derivative}")
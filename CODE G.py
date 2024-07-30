import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    Approximates the integral of f(x) from a to b using the trapezoidal rule with n trapezoids.
    
    Parameters:
    f (function): The function to integrate.
    a (float): The start point of the integration.
    b (float): The end point of the integration.
    n (int): The number of trapezoids.
    
    Returns:
    float: The approximate integral of f(x) from a to b.
    """
    # Calculate the width of each trapezoid
    h = (b - a) / n
    
    # Calculate the sum of the first and last terms
    integral = 0.5 * (f(a) + f(b))
    
    # Sum the middle terms
    for i in range(1, n):
        integral += f(a + i * h)
    
    # Multiply by the width of the trapezoids
    integral *= h
    
    return integral

# Example function to integrate
def f(x):
    return np.sin(x)

# Define the limits of integration
a = 0
b = np.pi

# Define the number of trapezoids
n = 1000

# Calculate the integral
integral = trapezoidal_rule(f, a, b, n)

print(f"The approximate integral of sin(x) from {a} to {b} using {n} trapezoids is {integral:.6f}")
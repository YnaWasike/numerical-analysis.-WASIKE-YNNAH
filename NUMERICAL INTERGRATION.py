import scipy.integrate as spi

# Define the function to integrate
def f(x):
    return x**2 + 3*x + 2

# Perform the integration from 0 to 1
result, error = spi.quad(f, 0, 1)

print(f"Integral result: {result}, Estimated error: {error}")
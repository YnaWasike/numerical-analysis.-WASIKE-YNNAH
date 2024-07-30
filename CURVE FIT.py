import numpy as np
from scipy.optimize import curve_fit

# Sample data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([2, 4, 6, 7, 10, 11])

# Define the model function
def model(x, a, b):
    return a * x + b

# Fit the model to the data
params, covariance = curve_fit(model, x_data, y_data)

print(f"Fitted parameters: {params}")
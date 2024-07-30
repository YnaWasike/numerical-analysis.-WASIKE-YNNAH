import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
x_data = np.array([[0], [1], [2], [3], [4], [5]])
y_data = np.array([2, 4, 6, 7, 10, 11])

# Create and fit the model
model = LinearRegression().fit(x_data, y_data)

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

print(f"Slope: {slope}, Intercept: {intercept}")
# Known points (x1, y1) and (x2, y2)
x1, y1 = 2.00, 7.2
x2, y2 = 4.25, 7.1

# The x value at which we want to interpolate
x = 4.0

# Linear interpolation formula
y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)

print(f"The value of y at x = {x} is {y:.2f}")

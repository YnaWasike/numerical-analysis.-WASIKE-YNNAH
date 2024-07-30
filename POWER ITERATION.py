import numpy as np

def power_iteration(A, num_simulations: int):
    # Randomly initialize the vector
    b_k = np.random.rand(A.shape[0])
    
    for _ in range(num_simulations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # Calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        
        # Re normalize the vector
        b_k = b_k1 / b_k1_norm
        
    # The eigenvalue is the Rayleigh quotient
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k))
    
    return eigenvalue, b_k

# Define the matrix A
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

# Run power iteration
eigenvalue_power, eigenvector_power = power_iteration(A, 1000)

print("Power Iteration Method:")
print(f"Eigenvalue: {eigenvalue_power}")
print(f"Eigenvector: {eigenvector_power}")
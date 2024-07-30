def qr_algorithm(A, num_iterations: int):
    A_k = A.copy()
    
    for _ in range(num_iterations):
        # QR decomposition
        Q, R = np.linalg.qr(A_k)
        # Recompose A_k
        A_k = np.dot(R, Q)
    
    # Eigenvalues are the diagonal elements of A_k
    eigenvalues = np.diag(A_k)
    
    return eigenvalues

# Run QR algorithm
eigenvalues_qr = qr_algorithm(A, 100)

print("\nQR Algorithm:")
print(f"Eigenvalues: {eigenvalues_qr}")
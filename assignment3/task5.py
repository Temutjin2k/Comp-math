# Using Jacobi’s method, find all the eigenvalues and the eigenvectors of the matrix:
#     1  √2  2
# A = √2 3  √2
#     2  √2  1

import math
import numpy as np

def jacobi_method(A, tolerance=1e-6, max_iterations=100):
    n = A.shape[0]
    V = np.eye(n) # Initialize the eigenvector matrix V as the identity matrix
    
    for iteration in range(max_iterations):
        max_val = 0
        p, q = 0, 0
        
        # Find the largest off-diagonal element in the matrix A
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j
    
        if max_val < tolerance:
            break
        
        theta = 0.5 * np.arctan2(2 * A[p, q], A[p, p] - A[q, q]) # Calculate the angle (theta) for the Jacobi rotation
        c, s = np.cos(theta), np.sin(theta)
        
        J = np.eye(n) # Create a rotation matrix J
        J[p, p], J[q, q] = c, c
        J[p, q], J[q, p] = s, -s
               
        A = np.dot(J.T, np.dot(A, J))  # Perform the rotation to update the matrix A
        V = np.dot(V, J)  # Update the eigenvectors matrix V
        
        # Print the results of each iteration
        print(f"Iteration {iteration + 1}:")
        print("Matrix A after rotation:")
        print(A)
        print("Eigenvectors matrix V:")
        print(V)
        print("Largest off-diagonal value:", max_val)
        print("------------------------------")
    
    # The eigenvalues are the diagonal elements of the matrix A
    eigenvalues = np.diag(A)
    return eigenvalues, V

# Define the matrix A
A = np.array([[1, math.sqrt(2), 2], [math.sqrt(2), 3, math.sqrt(2)], [2, math.sqrt(2), 1]])

# Call the Jacobi method to get eigenvalues and eigenvectors
eigenvalues, eigenvectors = jacobi_method(A)

# Print the final results
print("Jacobi's Method Result:")
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)


import numpy as np

# Define the matrix A
A = np.array([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
], dtype=float)

# Initial eigenvector guess
v = np.array([1, 0, 0], dtype=float)

# Parameters for the power method
max_iter = 1000  # Maximum number of iterations
tolerance = 1e-10  # Convergence threshold

# Power method iteration
for i in range(max_iter):
    # Compute the matrix-vector product
    v_next = np.dot(A, v)
    
    # Normalize the vector
    v_next_norm = np.linalg.norm(v_next)
    v_next = v_next / v_next_norm
    
    # Estimate the eigenvalue
    lambda_est = np.dot(v_next, np.dot(A, v_next))
    
    # Print the iteration details
    print(f"Iteration {i + 1}:")
    print(f"Eigenvector: {v_next}")
    print(f"Eigenvalue: {lambda_est}")
    print("-" * 30)
    
    # Check for convergence
    if np.linalg.norm(v_next - v) < tolerance:
        print(f"Converged in {i + 1} iterations.")
        break
    
    # Update the vector for the next iteration
    v = v_next

# Output the results
print("Final Results:")
print("Largest eigenvalue:", lambda_est)
print("Corresponding eigenvector:", v)

import numpy as np

A = np.array([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
], dtype=float)

v = np.array([1, 0, 0], dtype=float)

max_iter = 1000  
tolerance = 1e-10

for i in range(max_iter):
    v_next = np.dot(A, v)  # Compute the matrix-vector product

    v_next_norm = np.linalg.norm(v_next) # Normalize the vector
    v_next = v_next / v_next_norm
    lambda_est = np.dot(v_next, np.dot(A, v_next)) # Estimate the eigenvalue
    
    print(f"Iteration {i + 1}:")
    print(f"Eigenvector: {v_next}")
    print(f"Eigenvalue: {lambda_est}")
    print("-" * 30)
    
    if np.linalg.norm(v_next - v) < tolerance:  # Check for convergence
        print(f"Converged in {i + 1} iterations.")
        break
    
    v = v_next # Updating the vector

# Output the results
print("Final Results:")
print("Largest eigenvalue:", lambda_est)
print("Corresponding eigenvector:", v)

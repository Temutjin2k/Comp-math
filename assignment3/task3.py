# Apply iterative method to find more accurate inverse of A, 
# assuming the initial approximate inverse matrix B, where
#     1 10 1
# A = 2 0 1
#     3 3 2

#     0.4 2.4 −1.4
# B = 0.14 0.14 −0.14
#     −0.85 −3.8 2.8

import numpy as np

A = np.array([
    [1, 10, 1],
    [2,  0, 1],
    [3,  3, 2]
], dtype=float)

# Define the initial approximate inverse B
B = np.array([
    [0.4,  2.4, -1.4],
    [0.14, 0.14, -0.14],
    [-0.85, -3.8, 2.8]
], dtype=float)

# Identity matrix of the same size
I = np.eye(A.shape[0])

# Iterative refinement
tolerance = 1e-10  # Convergence threshold
max_iter = 1000    # Maximum number of iterations

for i in range(max_iter):
    # Compute residual R = I - AB
    R = I - np.dot(A, B)
    
    # Update B: B_new = B + BR
    B_new = B + np.dot(B, R)
    
    # Check for convergence
    if np.linalg.norm(R, ord=np.inf) < tolerance:
        print(f"Converged in {i} iterations.")
        break
    
    # Update B for the next iteration
    B = B_new

    # Printing each iteration
    print(f"iter: {i}\n{B}")

# Output 
print("Refined Inverse of A:")
print(B)

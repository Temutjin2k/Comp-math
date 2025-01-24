# Apply iterative method to find more accurate inverse of A, 
# assuming the initial approximate inverse matrix B, where
#     1 10 1
# A = 2 0 1
#     3 3 2

#     0.4 2.4 −1.4
# B = 0.14 0.14 −0.14
#     −0.85 −3.8 2.8

# Neumann series expansion:


import numpy as np

A = np.array([
    [1, 10, 1],
    [2,  0, 1],
    [3,  3, 2]
], dtype=float)

B = np.array([
    [0.4,  2.4, -1.4],
    [0.14, 0.14, -0.14],
    [-0.85, -3.8, 2.8]
], dtype=float)

I = np.eye(A.shape[0]) # Identity matrix

tolerance = 1e-10  
max_iter = 1000   

for i in range(max_iter):
    E = I - np.dot(A, B) # Compute residual E = I - AB
    B_new = B + np.dot(B, E) # Update B: B_new = B + BE
    
    if np.linalg.norm(E, ord=np.inf) < tolerance:  # Check for convergence
        print(f"Converged in {i} iterations.")
        break
    
    B = B_new
    print(f"iter: {i}\n{B}") # Printing each iteration

# Output 
print("Refined Inverse of A:")
print(B)

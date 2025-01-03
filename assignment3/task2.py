# Using the LU factorization method, find the inverse of the matrix A, where
#     50 107 36
# A = 35 54 20
#     31 66 21

import numpy as np
from scipy.linalg import lu

A = np.array([
    [50, 107, 36],
    [35, 54, 20],
    [31, 66, 21]
], dtype=float)

P, L, U = lu(A)  # P: permutation matrix, L: lower triangular, U: upper triangular
# Solve for the inverse
n = A.shape[0]
A_inv = np.zeros_like(A)
I = np.eye(n)

for i in range(n):
    # Solve Ly = e_i
    y = np.linalg.solve(L, I[:, i])
    # Solve Ux_i = y
    A_inv[:, i] = np.linalg.solve(U, y)

print("Matrix A:")
print(A)
print("\nLU decomposition:")
print("P:")
print(P)
print("L:")
print(L)
print("U:")
print(U)
print("\nInverse of A:")
print(A_inv)

import numpy as np
import pandas as pd

# Define the system of equations
A = np.array([
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
], dtype=float)

b = np.array([18, 26, 34, 82], dtype=float)

def make_diagonally_dominant(A, b):
    n = len(A)
    for i in range(n):
        row = abs(A[i])
        diag_index = np.argmax(row)
        if diag_index != i:
            A[[i, diag_index]] = A[[diag_index, i]]
            b[[i, diag_index]] = b[[diag_index, i]]
    return A, b

# Ensure A is diagonally dominant
A, b = make_diagonally_dominant(A, b)

# Helper functions for solving methods
def cramer_method(A, b):
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("System has no unique solution")

    solutions = []
    for i in range(A.shape[1]):
        A_i = A.copy()
        A_i[:, i] = b
        solutions.append(np.linalg.det(A_i) / det_A)

    return np.array(solutions)

def gauss_elimination(A, b):
    n = len(b)
    aug_matrix = np.hstack((A, b.reshape(-1, 1)))

    # Forward elimination
    for i in range(n):
        for j in range(i + 1, n):
            factor = aug_matrix[j, i] / aug_matrix[i, i]
            aug_matrix[j, i:] -= factor * aug_matrix[i, i:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (aug_matrix[i, -1] - np.dot(aug_matrix[i, i + 1:n], x[i + 1:n])) / aug_matrix[i, i]

    return x

def jacobi_method(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()
    iterations = []

    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_except_i = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_except_i) / A[i, i]

        iterations.append(x_new.copy())
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return np.array(iterations), x_new

        x = x_new

    raise ValueError("Jacobi method did not converge")

def gauss_seidel_method(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()
    iterations = []

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_except_i = sum(A[i, j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_except_i) / A[i, i]

        iterations.append(x_new.copy())
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return np.array(iterations), x_new

        x = x_new

    raise ValueError("Gauss-Seidel method did not converge")

# Solving using each method
cramer_result = cramer_method(A, b)
gauss_result = gauss_elimination(A, b)

x0 = np.zeros_like(b)
try:
    jacobi_iterations, jacobi_result = jacobi_method(A, b, x0)
except ValueError as e:
    print(f"Jacobi method error: {e}")
    jacobi_iterations, jacobi_result = None, None

try:
    gauss_seidel_iterations, gauss_seidel_result = gauss_seidel_method(A, b, x0)
except ValueError as e:
    print(f"Gauss-Seidel method error: {e}")
    gauss_seidel_iterations, gauss_seidel_result = None, None

# Formatting the iteration tables
if jacobi_iterations is not None:
    jacobi_table = pd.DataFrame(jacobi_iterations, columns=["x1", "x2", "x3", "x4"], index=range(1, len(jacobi_iterations) + 1))
    print("Jacobi Iteration Table:")
    print(jacobi_table)
else:
    print("Jacobi method did not produce iterations.")

if gauss_seidel_iterations is not None:
    gauss_seidel_table = pd.DataFrame(gauss_seidel_iterations, columns=["x1", "x2", "x3", "x4"], index=range(1, len(gauss_seidel_iterations) + 1))
    print("\nGauss-Seidel Iteration Table:")
    print(gauss_seidel_table)
else:
    print("Gauss-Seidel method did not produce iterations.")

# Final comparison table
comparison_data = {
    "Method": ["Cramer", "Gauss Elimination", "Jacobi", "Gauss-Seidel"],
    "x1": [cramer_result[0], gauss_result[0], jacobi_result[0] if jacobi_result is not None else None, gauss_seidel_result[0] if gauss_seidel_result is not None else None],
    "x2": [cramer_result[1], gauss_result[1], jacobi_result[1] if jacobi_result is not None else None, gauss_seidel_result[1] if gauss_seidel_result is not None else None],
    "x3": [cramer_result[2], gauss_result[2], jacobi_result[2] if jacobi_result is not None else None, gauss_seidel_result[2] if gauss_seidel_result is not None else None],
    "x4": [cramer_result[3], gauss_result[3], jacobi_result[3] if jacobi_result is not None else None, gauss_seidel_result[3] if gauss_seidel_result is not None else None]
}
comparison_table = pd.DataFrame(comparison_data)

print("\nComparison Table:")
print(comparison_table)

import numpy as np
from cramer import cramer_method
from gauss import gauss_method
from jacobi import jacobi_method
from gauss_seidel import gauss_seidel_method
from determinants import det_4x4

def solve_using_methods(A, b):
    """
    Solves the system of linear equations Ax = b using multiple methods and compares their results.
    """
    methods = [
        ("Cramer", cramer_method),
        ("Gauss", gauss_method),
        ("Jacobi", jacobi_method),
        ("Gauss-Seidel", gauss_seidel_method)
    ]
    
    results = {}
    print("Original system:")
    print("Matrix A:")
    print(A)
    print("Vector b:", b)
    print("\nSolutions by different methods:")

    # Attempt to solve the system using each method
    for name, method in methods:
        try:
            result = method(A, b)
            if result is None:
                print(f"\nMethod {name}: Did not converge")
            else:
                results[name] = np.array(result)
                print(f"\nMethod {name}:")
                print(results[name])
        except Exception as e:
            print(f"\nMethod {name}: Error - {str(e)}")

    return results


# Task
A = np.array([
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
], dtype=float)

b = np.array([18, 26, 34, 82], dtype=float)

results = solve_using_methods(A, b)


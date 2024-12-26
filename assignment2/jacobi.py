import numpy as np
from is_diagonally_dominant import is_diagonally_dominant

def jacobi_method(A, b, max_iter=1000, tol=1e-10):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    if not is_diagonally_dominant(A):

        P = np.eye(n)
        for i in range(n):
            max_row = i + np.argmax(np.abs(A[i:, i]))
            if max_row != i:
                A[[i, max_row]] = A[[max_row, i]]
                b[[i, max_row]] = b[[max_row, i]]
                P[[i, max_row]] = P[[max_row, i]]
        print("\nSolving with jacobi method\nMatrix A, b after turning diogonall dominant:")
        print("A:", A)
        print("b:",b)
    
    D = np.diag(A)
    if np.any(np.abs(D) < tol):
        return None  
    
    R = A - np.diagflat(D)
    x = np.zeros(n)
    
    
    iter_num = 0
    for i in range(max_iter):
        iter_num = i

        x_new = (b - np.dot(R, x)) / D
        if np.allclose(x, x_new, rtol=tol):
            print("Iterations for jacobi_method:", i)
            return x_new
        x = x_new
        
        if np.any(np.isnan(x)) or np.any(np.abs(x) > tol):
            print("Iterations for jacobi_method:", i)
            return None
        
    print("Iterations for jacobi_method:", iter_num + 1)
    return None  
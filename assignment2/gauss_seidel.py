import numpy as np
from is_diagonally_dominant import is_diagonally_dominant

def gauss_seidel_method(A, b, max_iter=1000, tol=1e-10):
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
        print("\nSolving with gauss-seidel method\nMatrix A, b after turning diogonall dominant:")
        print("A:", A)
        print("b:",b)
    
    if np.any(np.abs(np.diag(A)) < 1e-10):
        return None
        
    x = np.zeros(n)
    
    iter_num = 0

    for iter_count in range(max_iter):
        iter_num = i

        x_new = np.zeros(n)
        for i in range(n):
            s1 = np.dot(A[i,:i], x_new[:i])
            s2 = np.dot(A[i,i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i,i]
        
        if np.allclose(x, x_new, rtol=tol):
            print("Iterations for gauss_seidel method:", iter_num)
            return x_new
            
        if np.any(np.isnan(x_new)) or np.any(np.abs(x_new) > 1e6):
            print("Iterations for gauss_seidel method:", iter_num)
            return None
        
        x = x_new
    print("Iterations for gauss_seidel method:", iter_num)
    return None  
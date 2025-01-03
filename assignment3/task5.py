# Using Jacobi’s method, find all the eigenvalues and the eigenvectors of the matrix:
#     1  √2  2
# A = √2 3  √2
#     2  √2  1


import numpy as np

def jacobi_method(A, max_iter=100, tol=1e-10):
    A = np.array(A, dtype=float)
    n = A.shape[0]
    
    # Начальная матрица и собственные векторы
    eig_vals = np.diagonal(A)
    eig_vecs = np.eye(n)
    
    for i in range(max_iter):
        # Находим максимальный элемент вне диагонали
        off_diagonal = np.abs(A - np.diag(np.diagonal(A)))
        max_val = np.max(off_diagonal)
        
        if max_val < tol:
            break
        
        # Ищем индексы для максимального элемента
        p, q = np.unravel_index(np.argmax(off_diagonal), A.shape)
        
        # Если p == q, продолжаем
        if A[p, p] == A[q, q]:
            continue
        
        # Вычисляем угол поворота
        if A[p, p] != A[q, q]:
            theta = 0.5 * np.arctan(2 * A[p, q] / (A[p, p] - A[q, q]))
        else:
            theta = np.pi / 4
        
        # Создаем матрицу поворота
        R = np.eye(n)
        R[p, p] = R[q, q] = np.cos(theta)
        R[p, q] = -np.sin(theta)
        R[q, p] = np.sin(theta)
        
        # Обновляем матрицу A и собственные векторы
        A = np.dot(np.dot(R.T, A), R)
        eig_vecs = np.dot(eig_vecs, R)
        print("Iteration", i)
        print(A)
        print(eig_vecs)
    
    eig_vals = np.diagonal(A)
    
    return eig_vals, eig_vecs

# Матрица A
A = np.array([
    [1, np.sqrt(2), 2],
    [np.sqrt(2), 3, np.sqrt(2)],
    [2, np.sqrt(2), 1]
])

eigenvalues, eigenvectors = jacobi_method(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

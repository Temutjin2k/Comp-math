import numpy as np

def gauss_method(A, B):
    augmented_matrix = np.column_stack((A, B))  
    rows, cols = augmented_matrix.shape

    print("\n Method gauss's step")    
    for i in range(rows):
        print(i, augmented_matrix)
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i  
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]  
        augmented_matrix[i] /= augmented_matrix[i, i]  

        # subtacting elements under pivot
        for j in range(i + 1, rows):
            augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i] 
         

    x = np.zeros(rows)
    # finding all valeus for x
    for i in range(rows - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.sum(augmented_matrix[i, i + 1:cols - 1] * x[i + 1:])
    
    return x

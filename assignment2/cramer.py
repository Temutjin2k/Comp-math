from determinants import det_4x4

def cramer_method(A, B):
    print("Starting cramer's method:")
    det_A = det_4x4(A)
    if det_A == 0:
        return "The system of equations is inconsistent."
    
    solutions = []

    print("Determinant", det_A)
    for i in range(4):
        A_copy = A.copy()
        A_copy[:, i] = B
        det_A_i = det_4x4(A_copy)
        print("Det(Ai):", det_A_i)
        solutions.append(det_A_i / det_A)
    return solutions

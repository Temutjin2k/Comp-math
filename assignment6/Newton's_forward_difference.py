import numpy as np

def newton_forward_difference(x, y, h):
    n = len(y)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i + 1, j - 1] - diff_table[i, j - 1]

    first_derivative = (diff_table[0, 1] - (diff_table[0, 2] / 2) + (diff_table[0, 3] / 3)) / h
    second_derivative = (diff_table[1, 2] - diff_table[0, 2]) / (h ** 2)
    return first_derivative, second_derivative, diff_table

f = lambda x: x ** 3 + 3 * x + 2

x_values = np.array([-2, -1,3,4])

h = x_values[1] - x_values[0]
y_values = f(x_values)

print("x values:",x_values)
print("y values:",y_values)

first_deriv, second_deriv, diff_table = newton_forward_difference(x_values, y_values, h)

print(f"First derivative at x = {x_values[0]}: {first_deriv:.4f}")
print(f"Second derivative at x = {x_values[0]}: {second_deriv:.4f}")

print("\nNewton's Forward Difference Table:")
print(diff_table)
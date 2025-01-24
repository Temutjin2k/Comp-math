def newton_divided_difference_interpolation(x, y, value):
    n = len(x)

    dd_table = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        dd_table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            dd_table[i][j] = (dd_table[i + 1][j - 1] - dd_table[i][j - 1]) / (x[i + j] - x[i])

    res = y[0]
    temp = 1

    for i in range(1, n):
        temp *= (value - x[i - 1])
        res += temp * dd_table[0][i]

    return res

x = [2, 3, 6, 7, 9]  # x-coordinates of data points
y = [15, 39, 243, 375, 771]  # y-coordinates of data points
value = 5  # The x-value at which to interpolate

print("newton divided method")
result = newton_divided_difference_interpolation(x, y, value)
print(f"The interpolated value at x = {value} is {result}")
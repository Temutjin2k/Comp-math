def PrintTable(array):
    for i in array:
        print(i)



def newton_forward_interpolation(x, y, value):
    n = len(x)

    h = x[1] - x[0]
    u = (value - x[0]) / h

    diff_table = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        diff_table[i][0] = y[i]


    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    PrintTable(diff_table)
    res = y[0]
    u_term = 1
    for i in range(1, n):
        u_term *= (u - (i - 1))
        res += (u_term * diff_table[0][i]) / factorial(i)
        print("#",i, '\n', res)

    return res

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# x = [2, 3, 4, 5]  # x-coordinates of data points
# y = [14.5, 16.3, 17.5, 18]  # y-coordinates of data points
# value = 2.5  # The x-value at which to interpolate

# x = [3, 5, 7, 9]  # x-coordinates of data points
# y = [180, 150, 120, 90]  # y-coordinates of data points
# value = 4  # The x-value at which to interpolate

x = [0, 1, 2, 3, 4]
y = [1, 8, 27, 64, 125]
value = 2.5  # The x-value at which to interpolate

print("Newton Forward method")
result = newton_forward_interpolation(x, y, value)
print(f"The interpolated value at x = {value} is {result}")
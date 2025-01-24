def lagrange_interpolation(x, y, value):
    n = len(x)
    res = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (value - x[j]) / (x[i] - x[j])
        res += term
        
    return res

x = [0, 2, 3, 5, 6]  # x-coordinates of data points
y = [5, 7, 8, 10, 12]  # y-coordinates of data points
value = 4  # The x-value at which to interpolate

print("lagrange_interpolation")
result = lagrange_interpolation(x, y, value)
print(f"The interpolated value at x = {value} is {result}")
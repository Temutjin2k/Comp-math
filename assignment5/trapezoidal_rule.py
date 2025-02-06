def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        result += 2 * func(x)

    result *= h / 2
    return result

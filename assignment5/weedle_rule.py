def weedle_rule(func, a, b, n):
    if n % 6 != 0:
        return None
    
    h = (b - a) / n
    result = 0

    for i in range(1, n):
        x = a + i * h
        if i % 6 == 1 or i % 6 == 5:
            result += 5 * func(x)
        elif i % 6 == 2 or i % 6 == 4:
            result += func(x)
        elif i % 6 == 3:
            result += 6 * func(x)
        elif i % 6 == 0:
            result += 2 * func(x)

    result *= 3 * h / 10
    return result

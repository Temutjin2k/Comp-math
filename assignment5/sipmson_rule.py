def simpson_rule_1_3(func, a, b, n):
    if n % 2:
        return None
        
    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * func(x)
        else:
            result += 4 * func(x)

    result *= h / 3
    return result

def simpson_rule_3_8(func, a, b, n):
    if n % 3 == 0:
        return None

    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            result += 2 * func(x)
        else:
            result += 3 * func(x)

    result *= 3 * h / 8
    return result

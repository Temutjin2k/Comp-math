import math

def secant_method(f, x0, x1, tol, max_iter=100):
    """ Secant method """
    for i in range(max_iter):
        if abs(f(x1) - f(x0)) < 1e-10:
            break
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_temp - x1) < tol:
            return round(x_temp, 3), i+1
        x0, x1 = x1, x_temp
    return None, i

def newton_raphson_method(f, df, x0, tol, max_iter=100):
    """ Newton-Raphson method"""

    for i in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return round(x1, 3), i+1
        x0 = x1
    return None, i

def iteration(g, x0, tol, max_iter=100):
    """ Iteration method  """
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return round(x1, 3), i+1
        x0 = x1
    return None, i

# def bisection():


def comparative_analysis():
    # Define equations and derivatives
    equations = [
        {   # (i) x^3 - x - 1 = 0
            'eq': "x^3 - x - 1 = 0",
            'f': lambda x: x**3 - x - 1,
            'df': lambda x: 3*x**2 - 1,
            'g': lambda x: (x + 1)**(1/3),
            'x0': 1.0, 'x1': 1.5
        },
        {   # (ii) x - cos(x) = 0
            'eq': "x - cos(x)",
            'f': lambda x: x - math.cos(x),
            'df': lambda x: 1 + math.sin(x),
            'g': lambda x: math.cos(x),
            'x0': 0.5, 'x1': 0.7
        },
        {   # (iii) e^(-x) - x = 0
            'eq': "e^(-x) - x",
            'f': lambda x: math.exp(-x) - x,
            'df': lambda x: -math.exp(-x) - 1,
            'g': lambda x: math.exp(-x),
            'x0': 0.5, 'x1': 0.7
        },
        {   # (iv) x^3 + x^2 + x + 7 = 0
            'eq': "x^3 + x^2 + x + 7",
            'f': lambda x: x**3 + x**2 + x + 7,
            'df': lambda x: 3*x**2 + 2*x + 1,
            'g': lambda x: -((x**2 + x + 7)**(1/3)),
            'x0': -2.0, 'x1': -1.5
        },
        {   # (v) x^2 + 4*sin(x) = 0
            'eq': "x^2 + 4*sin(x)",
            'f': lambda x: x**2 + 4*math.sin(x),
            'df': lambda x: 2*x + 4*math.cos(x),
            'g': lambda x: -math.sqrt(-4*math.sin(x)) if -4*math.sin(x) > 0 else x,
            'x0': -1.0, 'x1': -0.5
        },
        {   # (vi) cos(x) - x*e^x = 0
            'eq': "cos(x) - x*e^x",
            'f': lambda x: math.cos(x) - x*math.exp(x),
            'df': lambda x: -math.sin(x) - math.exp(x) - x*math.exp(x),
            'g': lambda x: math.cos(x) / math.exp(x),
            'x0': 0.5, 'x1': 0.7
        }
    ]

    max_iter=100
    tol=1e-8

    # Table header
    print(f"Max iter: {max_iter}")
    print(f"Tolerance: {tol}")
    print(f"{'Root'}| {'Secant'} | {'Newton'} | {'Iteration'} | secant_iter | newton_iter | iterationM_iter")
    print("-"*40)

    # Solve and print results for each equation
    for i, eq in enumerate(equations, start=1):
        secant_root, si = secant_method(eq['f'], eq['x0'], eq['x1'], tol, max_iter)
        newton_root, ni = newton_raphson_method(eq['f'], eq['df'], eq['x0'], tol, max_iter)
        iteration_root, ii = iteration(eq['g'], eq['x0'], tol, max_iter)
        print(f"  x{i}  | {secant_root} | {newton_root} | {iteration_root}  |      {si}      |      {ni}      |     {ii}    ")


comparative_analysis()

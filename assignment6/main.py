import math

def exact_solution(x):
    return 2 * math.exp(x) - x - 1

def euler_method(f, x0, y0, h, steps):
    x_vals = [x0]
    y_vals = [y0]
    for _ in range(steps):
        y0 = y0 + h * f(x0, y0)
        x0 += h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

def modified_euler_method(f, x0, y0, h, steps):
    x_vals = [x0]
    y_vals = [y0]
    for _ in range(steps):
        y_pred = y0 + h * f(x0, y0)
        y_corr = y0 + (h / 2) * (f(x0, y0) + f(x0 + h, y_pred))
        x0 += h
        y0 = y_corr
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

def runge_kutta_3rd(f, x0, y0, h, steps):
    x_vals = [x0]
    y_vals = [y0]
    for _ in range(steps):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h, y0 - k1 + 2 * k2)
        y0 = y0 + (k1 + 4 * k2 + k3) / 6
        x0 += h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

def runge_kutta_4th(f, x0, y0, h, steps):
    x_vals = [x0]
    y_vals = [y0]
    for _ in range(steps):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 += h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

def func(x, y):
    return x + y

# Parameters
x0, y0, h, steps = 0, 1, 0.01, 50

x_vals_euler, y_vals_euler = euler_method(func, x0, y0, h, steps)
x_vals_modified_euler, y_vals_modified_euler = modified_euler_method(func, x0, y0, h, steps)
x_vals_rk3, y_vals_rk3 = runge_kutta_3rd(func, x0, y0, h, steps)
x_vals_rk4, y_vals_rk4 = runge_kutta_4th(func, x0, y0, h, steps)

print(f"{'x':<8} {'Exact Solution':<25} {'Euler':<20} {'Modified Euler':<25} {'Runge Kutta 3rd':<25} {'Runge Kutta 4th':<25}")

for x, exact, euler, modified_euler, rk3, rk4 in zip(x_vals_euler, [exact_solution(x) for x in x_vals_euler], y_vals_euler, y_vals_modified_euler, y_vals_rk3, y_vals_rk4):
    print(f"{x:<8.2f} {exact:<25.10f} {euler:<20.10f} {modified_euler:<25.10f} {rk3:<25.10f} {rk4:<25.10f}")

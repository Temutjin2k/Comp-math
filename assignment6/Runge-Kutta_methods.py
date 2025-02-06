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

def func1(x, y):
    return x + y

x0, y0, h, steps = 0, 1, 0.1, 2
x_vals_3rd, y_vals_3rd = runge_kutta_3rd(func1, x0, y0, h, steps)

print("Runge-Kutta 3rd order:")
for i in range(len(x_vals_3rd)):
    print("Step:", i, "| x:", round(x_vals_3rd[i], 3), "| y:", round(y_vals_3rd[i], 5))

def func2(x, y):
    return x**2 - y

x0, y0, h, steps = 0, 1, 0.1, 2
x_vals_4th, y_vals_4th = runge_kutta_4th(func2, x0, y0, h, steps)

print("\nRunge-Kutta 4th order:")
for i in range(len(x_vals_4th)):
    print("Step:", i, "| x:", round(x_vals_4th[i], 3), "| y:", round(y_vals_4th[i], 5))

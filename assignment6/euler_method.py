#Chapter 10, exercises 10.2, task 3
def euler_method(f, x0, y0, h, steps):
    x_vals = [x0]
    y_vals = [y0]
    for _ in range(steps):
        y0 = y0 + h * f(x0, y0)
        x0 += h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

def func(x, y):
    return x + y + x * y

x0 = 0
y0 = 1
h = 0.025
steps = 4

x_vals, y_vals = euler_method(func, x0, y0, h, steps)
table = list(zip(x_vals, y_vals))

for i in range(len(x_vals)):
    print("Step:", i, "x:", round(x_vals[i], 3), "y:", round(y_vals[i], 5))


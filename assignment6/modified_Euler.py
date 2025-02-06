#Chapter 10, exercises 10.2, task 5
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

def func(x, y):
    return x ** 2 + y

x0 = 0
y0 = 1
h = 0.05
steps = 2

x_vals, y_vals = modified_euler_method(func, x0, y0, h, steps)
table = list(zip(x_vals, y_vals))

for i in range(len(x_vals)):
    print("x:", round(x_vals[i], 2), "| y:", round(y_vals[i], 5))

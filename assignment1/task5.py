import matplotlib.pyplot as plt

def f(x): return x**3 - x - 1
def df(x): return 3*x**2 - 1

def newton_raphson_absolute_error(f, df, x0, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        x_new = x0 - f(x0) / df(x0)
        abs_error = abs(x_new - x0)
        print(f"Iteration {i+1}: x = {x_new}, Absolute Error = {abs_error}")
        if abs_error < tol:
            return x_new
        x0 = x_new
    return None

root = newton_raphson_absolute_error(f, df, 1.5)
print("Found root: ", root)

def newton_raphson_relative_error(f, df, x0, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        x_new = x0 - f(x0) / df(x0)
        rel_error = abs(x_new - x0) / abs(x0)
        print(f"Iteration {i+1}: x = {x_new}, Relative Error = {rel_error}")
        if rel_error < tol:
            return x_new
        x0 = x_new
    return None

root = newton_raphson_relative_error(f, df, 1.5)
print("Found root: ",root)

def newton_raphson_error_tracking(f, df, x0, tol=1e-5, max_iter=100):
    abs_errors = []
    rel_errors = []
    for i in range(max_iter):
        x_new = x0 - f(x0) / df(x0)
        abs_error = abs(x_new - x0)
        rel_error = abs(x_new - x0) / abs(x0)
        abs_errors.append(abs_error)
        rel_errors.append(rel_error)
        if abs_error < tol:
            break
        x0 = x_new
    return abs_errors, rel_errors

abs_errors, rel_errors = newton_raphson_error_tracking(f, df, 1.5)

plt.figure(figsize=(10, 6))
plt.plot(abs_errors, label='Absolute Error')
plt.plot(rel_errors, label='Relative Error')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Comparison of Absolute and Relative Errors (Newton-Raphson)')
plt.legend()
plt.grid(True)
plt.show()

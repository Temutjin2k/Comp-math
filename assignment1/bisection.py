import math

def fn(x):
    return math.exp(x) - x**2

# Bisection
def bis(a, b, tol, nmax):
    i = 0  
    while i < nmax:
        c = (a + b) / 2  

        if fn(c) == 0 or abs(fn(c)) < tol: 
            return c
        
        if fn(a) * fn(c) > 0:  
            a = c
        else:
            b = c
        i += 1  
    return (a + b) / 2  

# Initial parameters
a = -2
b = 0
tol = 10**(-2)
nmax = 7

root = bis(a, b, tol, nmax)
print(f"Approximate root: {root}")

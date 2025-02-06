from trapezoidal_rule import trapezoidal_rule
from sipmson_rule import simpson_rule_1_3, simpson_rule_3_8
from boole_rule import boole_rule
from weedle_rule import weedle_rule
import math

def f(x):
    return x**3 + x**2 + 3*x + 45

a = 0
b = 8
n = 12

trapezoidal= trapezoidal_rule(f, a, b, n)
simpson13 = simpson_rule_1_3(f, a, b, n)
simpson38 = simpson_rule_3_8(f, a, b, n)
boole = boole_rule(f, a, b, n)
weedle = weedle_rule(f, a, b, n)

print("Trapezoidal Rule:",trapezoidal)
print("Simpson’s one-third rule:", simpson13)
print("Simpson’s three-eighth rule:", simpson38)
print("Boole’s Rule:", boole)
print("Weddle’s Rule:",weedle)

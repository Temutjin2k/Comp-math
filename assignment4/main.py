from newton_forward import newton_forward_interpolation
from lagrange import lagrange_interpolation
from newton_divided import newton_divided_difference_interpolation

# x = [2, 3, 4, 5]
# y = [14.5, 16.3, 17.5, 18]
# value = 2.5
# result = newton_forward_interpolation(x, y, value)
# print(f"Using Newton's forward interpolation formula x = {value} is {result}")

# x = [0, 2, 3, 5, 6]
# y = [5, 7, 8, 10, 12]
# value = 4
# result = lagrange_interpolation(x, y, value)
# print(f"Using Lagrange's interpolation formula x = {value} is {result}")

# x = [2, 3, 6, 7, 9]
# y = [15, 39, 243, 375, 771]
# value = 5
# result = newton_divided_difference_interpolation(x, y, value)
# print(f"Using Newton's divided difference formula x = {value} is {result}")

# x = [2, 3, 4, 5]
# y = [14.5, 16.3, 17.5, 18]
# value = 2.5

x = [1, 2, 3, 4, 5]
y = [30, 15, 32, 18, 25]
value = 2.5

res1 = newton_forward_interpolation(x, y, value)
res2 = lagrange_interpolation(x, y, value)
res3 = newton_divided_difference_interpolation(x, y, value)
print(f"Using Newton's forward interpolation formula x = {value} is {res1}")
print(f"Using Lagrange's interpolation formula x = {value} is {res2}")
print(f"Using Newton's divided difference formula x = {value} is {res3}")

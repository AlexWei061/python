from sympy import *
import time

# "SEND + MORE = MONEY"

x = Symbol('x')

result = solve(pow(x, 3) - 1, x)

print("the answer is:" + str(result))
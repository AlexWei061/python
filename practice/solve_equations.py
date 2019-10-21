from sympy import *
import time

x = Symbol('x')

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

result = solve(x*x*x-1,x)
print("solving...")
time.sleep(3)

print("the answer is:" + str(result))
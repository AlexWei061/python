from sympy import *
import time

# "SEND + MORE = MONEY"

S = Symbol("S")
E = Symbol("E")
N = Symbol("N")
D = Symbol("D")
M = Symbol("M")
O = Symbol("O")
R = Symbol("R")
Y = Symbol("Y")

result = solve(1000*S + 100*E + 10*N + D + 1000*M + 100*O + 10*R + E - 10000*M - 1000*O - 100*N - 10*E - Y,S)
print("solving...")
time.sleep(3)

print("the answer is:" + str(result))
import numpy as np
from matplotlib import pyplot as plt
import time
import random

n = 6400
m = 200
data = np.arange(0, n)

"""
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.xlim(0, 35)
plt.ylim(0, 35)
plt.plot(x, y)
"""

def showLines():
    for i in range(9):
        ax.plot(data, data * 0 + 800 * i, color = 'balck')
        ax.plot(data * 0 + 800 * i, data, color = 'dodgerblue')

plt.ion()

figure, ax = plt.subplots(figsize = (8, 6))

plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.xlim(0, n)
plt.ylim(0, n)
x = []
y = []

for i in range(0, m):
    # random.seed(time.time())
    x.append(random.random() * n)
    y.append(random.random() * n)
random.seed(time.time())

while 1:
    for i in range(0, m):
        rd = random.random()
        if(rd > 0.5):
            x[i] = (x[i] + random.random() * 10) % n
        else:
            x[i] = (x[i] - random.random() * 10) % n
        rd = random.random()
        if (rd > 0.5):
            y[i] = (y[i] + random.random() * 10) % n
        else:
            y[i] = (y[i] - random.random() * 10) % n

    ax.clear()
    showLines()
    ax.scatter(x, y, color='r', marker='.')

    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.pause(0.01)

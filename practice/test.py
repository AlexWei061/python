import numpy as np
from matplotlib import pyplot as plt
import time
import random

mapSize = 6400                                  # 地图大小
peopleNum = 200                                 # 总人数
data = np.arange(0, mapSize)

def Random(mu, sigma):                          # 正态分布 让每一次人们的移动方向大概率相同
    return np.random.normal(mu, sigma, 1)

def showLines():
    for i in range(int(mapSize / 800) + 1):
        ax.plot(data, data * 0 + 800 * i, color = 'grey')
        ax.plot(data * 0 + 800 * i, data, color = 'grey')

def initmap():
    plt.title("MAP")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.xlim(0, mapSize)
    plt.ylim(0, mapSize)

plt.ion()
figure, ax = plt.subplots(figsize = (8, 6))

# green
gx = []                                                    # x 和 y 是坐标
gy = []
gdire = []                                                 # 每个人的移动方向
gtime = []                                                 # 每个人在同一个区块停留的时间
gpre = []                                                  # 上一个时间内所在的区块编号
# red
rx = []
ry = []
rdire = []
rtime = []
rpre = []
# yellow
yx = []
yy = []
ydire = []
ytime = []
ypre = []

block = [
    [0,   800,  0,  800], [0,    800,  800, 1600], [0,    800,  1600, 2400], [0,    800,  2400, 3200], [0,    800,  3200, 4000], [0,    800,  4000, 4800], [0,    800,  4800, 5600], [0,    800,  5600, 6400],
    [800,  1600, 0, 800], [800,  1600, 800, 1600], [800,  1600, 1600, 2400], [800,  1600, 2400, 3200], [800,  1600, 3200, 4000], [800,  1600, 4000, 4800], [800,  1600, 4800, 5600], [800,  1600, 5600, 6400],
    [1600, 2400, 0, 800], [1600, 2400, 800, 1600], [1600, 2400, 1600, 2400], [1600, 2400, 2400, 3200], [1600, 2400, 3200, 4000], [1600, 2400, 4000, 4800], [1600, 2400, 4800, 5600], [1600, 2400, 5600, 6400],
    [2400, 3200, 0, 800], [2400, 3200, 800, 1600], [2400, 3200, 1600, 2400], [2400, 3200, 2400, 3200], [2400, 3200, 3200, 4000], [2400, 3200, 4000, 4800], [2400, 3200, 4800, 5600], [2400, 3200, 5600, 6400],
    [3200, 4000, 0, 800], [3200, 4000, 800, 1600], [3200, 4000, 1600, 2400], [3200, 4000, 2400, 3200], [3200, 4000, 3200, 4000], [3200, 4000, 4000, 4800], [3200, 4000, 4800, 5600], [3200, 4000, 5600, 6400],
    [4000, 4800, 0, 800], [4000, 4800, 800, 1600], [4000, 4800, 1600, 2400], [4000, 4800, 2400, 3200], [4000, 4800, 3200, 4000], [4000, 4800, 4000, 4800], [4000, 4800, 4800, 5600], [4000, 4800, 5600, 6400],
    [4800, 5600, 0, 800], [4800, 5600, 800, 1600], [4800, 5600, 1600, 2400], [4800, 5600, 2400, 3200], [4800, 5600, 3200, 4000], [4800, 5600, 4000, 4800], [4800, 5600, 4800, 5600], [4800, 5600, 5600, 6400],
    [5600, 6400, 0, 800], [5600, 6400, 800, 1600], [5600, 6400, 1600, 2400], [5600, 6400, 2400, 3200], [5600, 6400, 3200, 4000], [5600, 6400, 4000, 4800], [5600, 6400, 4800, 5600], [5600, 6400, 5600, 6400]
]
def findblock(x, y):                                             # 找到这个坐标所在的区块编号
    for i in range(0, 64):
        if (block[i][0] <= x and x <= block[i][1]) and (block[i][2] <= y and y <= block[i][3]):
            return i


def initred():                                  # 选择一个被感染的 "幸运" 市民
    rd = np.random.randint(0, peopleNum)
    rx.append((gx[rd]))
    ry.append((gy[rd]))
    rdire.append((gdire[rd]))
    rtime.append((gtime[rd]))
    rpre.append(gpre[rd])
    del gx[rd]
    del gy[rd]
    del gdire[rd]
    del gtime[rd]
    del gpre[rd]

def dire():
    rd = np.random.randint(0, 3)
    if rd == 0:
        tempx = -1
    elif rd == 1:
        tempx = 1
    else:
        tempx = 0
    rd = np.random.randint(0, 3)
    if rd == 0:
        tempy = -1
    elif rd == 1:
        tempy = 1
    else:
        tempy = 0
    return [tempx, tempy]

def Initialize():
    initmap()                                                         # 初始化画布
    for i in range(0, peopleNum):                                     # 初始随机生成每个人的坐标
        gtime.append(0)
        gdire.append(dire())
        gx.append((Random(0, 0.5) * mapSize) % mapSize)
        gy.append((Random(0, 0.5) * mapSize) % mapSize)
        gpre.append(findblock(gx[i], gy[i]))
    initred()

def moveperson():
    # 为了让所有点都不超出地图的限制，我把所有的点的坐标进行微扰之后都对地图大小取模
    # 但是这样就会出现某一些点到达地图边界之后就从地图的另一端直接冒出来的情况
    for i in range(0, len(gx)):
        gx[i] = (gx[i] + Random(gdire[i][0], 0.5) * 10) % mapSize
        gy[i] = (gy[i] + Random(gdire[i][1], 0.5) * 10) % mapSize
    for i in range(0, len(rx)):
        rx[i] = (rx[i] + Random(rdire[i][0], 0.5) * 10) % mapSize
        ry[i] = (ry[i] + Random(rdire[i][1], 0.5) * 10) % mapSize
    for i in range(0, len(yx)):
        yx[i] = (yx[i] + Random(ydire[i][0], 0.5) * 10) % mapSize
        yy[i] = (yy[i] + Random(ydire[i][1], 0.5) * 10) % mapSize

def showgragh():
    ax.clear()
    showLines()
    ax.scatter(gx, gy, color="limegreen", marker=".")
    ax.scatter(rx, ry, color="red", marker=".")
    ax.scatter(yx, yy, color="yellow", marker=".")
    figure.canvas.draw()
    figure.canvas.flush_events()

def movegtoy(idx):
    yx.append((gx[idx]))
    yy.append((gy[idx]))
    ydire.append((gdire[idx]))
    ytime.append((gtime[idx]))
    ypre.append(gpre[idx])
    gx.pop(idx)
    gy.pop(idx)
    gdire.pop(idx)
    gtime.pop(idx)
    gpre.pop(idx)

def adjustcondition():
    for i in range(0, len(gx)):
        bidx = findblock(gx[i], gy[i])
        if bidx == gpre[i]:
            gtime[i] = gtime[i] + 1
        else:
            gtime[i] = 0
        gpre[i] = bidx

    for i in range(0, len(rx)):
        bidx = findblock(rx[i], ry[i])
        if bidx == rpre[i]:
            rtime[i] = rtime[i] + 1
        else:
            rtime[i] = 0
        rpre[i] = bidx
        if rtime[i] >= 10:
            for j, item in enumerate(gx):                      # 枚举所有的健康人
                bidx = findblock(gx[j], gy[j])
                if (bidx == rpre[i]) and (gtime[j] >= 15):     # 如果他和感染者在同一个区块而且他们共同停留时间超过 15
                    movegtoy(j)                                # 这个人将成为时空伴随者

    for i in range(0, len(yx)):
        bidx = findblock(yx[i], yy[i])
        if bidx == ypre[i]:
            ytime[i] = ytime[i] + 1
        else:
            ytime[i] = 0
        ypre[i] = bidx

def adjustdire():                                                   # 随即改变人们行走的方向
    for i in range(0, len(gx)):
        gdire[i] = dire()
    for i in range(0, len(rx)):
        rdire[i] = dire()
    for i in range(0, len(yx)):
        ydire[i] = dire()

if __name__ == '__main__':
    Initialize()
    time = 0
    while 1:
        time = time + 1
        if(time % 100 == 0):
            adjustdire()
        moveperson()
        adjustcondition()
        showgragh()
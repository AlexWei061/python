g1 = [89,78,69,89,32,111,21,70,62,100.43,93,96.67]

for x in range(0,len(g1)):
    for xx in range(x,len(g1)):
        if g1[xx] < g1[x]:
            num = g1[xx]
            g1[xx] = g1[x]
            g1[x] = num
print(g1)

for index in range(0,len(g1)):
    for sindex in range(index, len(g1)):
        if g1[sindex] > g1[index]:
            temp = g1[index]
            g1[index] = g1[sindex]
            g1[sindex] = temp
print(g1)
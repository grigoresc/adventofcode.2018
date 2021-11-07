
from functools import reduce
import re
from typing import Counter
txt = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

# inp = [line.strip() for line in txt.split('\n')]
inp = [line.strip() for line in open("input.txt", 'r')]


def parse(line):
    (x, y) = re.findall(r'\d+', line)
    return int(x), int(y)


def getSurroundingPositions(x, y, dist):
    for c in range(x-dist, x+dist+1):
        yield c, y-dist
    for c in range(x-dist, x+dist+1):
        yield c, y+dist
    for l in range(y-dist+1, y+dist):
        yield x-dist, l
    for l in range(y-dist+1, y+dist):
        yield x+dist, l


def getAllowedPositions(x, y, dist):
    if dist == 0:
        yield (x, y)
        return
    for pos in getSurroundingPositions(x, y, dist):
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < leng and pos[1] < leng:
            yield pos


def fillArea(dist):
    for i, c in enumerate(coords):
        (x, y) = c
        for px, py in getAllowedPositions(x, y, dist):
            manh = abs(px-x)+abs(py-y)
            if area[py][px][0] == None:
                area[py][px] = (i, manh)
            else:
                if area[py][px][1] == manh:
                    area[py][px] = (-1, manh)
                elif area[py][px][1] > manh:
                    area[py][px] = (i, manh)


coords = list(map(parse, inp))
leng = max(max(coords))+2  # todo +2? or 0 is enough..

# map with visible coord and min distance
area = [[(None, None) for i in range(leng)] for j in range(leng)]

for dist in range(0, leng-1):
    fillArea(dist)


def printm(lst, f):
    for line in lst:
        s = reduce(lambda x, y: x+f(y), line, "")
        print(s)

# printm(area, lambda x: chr(ord('A')+x[0]) if x[0] != None else '#')


cnts = [0 for i in range(0, len(coords))]

for y in range(0, leng):
    for x in range(0, leng):
        if area[y][x][0] >= 0:
            cnts[area[y][x][0]] += 1

margins = set()
for i in range(0, leng):
    margins.add(area[0][i][0])
    margins.add(area[leng-1][i][0])
    margins.add(area[i][0][0])
    margins.add(area[i][leng-1][0])

filter(lambda x: x not in margins, enumerate(cnts))
m = max(list(filter(lambda x: x[0] not in margins, list(
    enumerate(cnts)))), key=lambda x: x[1])
sln = m[1]
print(sln)
# 3620

from functools import reduce
import re
from typing import Counter

# inp = [line.strip() for line in open("sample.txt", 'r')]
inp = [line.strip() for line in open("input.txt", 'r')]


def parse(line):
    (v, x, y, z) = re.findall(r'-?\d+', line)
    return int(v), int(x), int(y), int(z)


points = list(map(parse, inp))


def increment(item):
    return (item[0]+item[2], item[1]+item[3], item[2], item[3])


next = points.copy()
predDiffy = 10000000
seconds = 0


def DiffsAndMins(next):
    miny = min(next, key=lambda x: x[1])[1]
    maxy = max(next, key=lambda x: x[1])[1]
    diffy = maxy - miny
    minx = min(next, key=lambda x: x[0])[0]
    maxx = max(next, key=lambda x: x[0])[0]
    diffx = maxx - minx
    return (diffx, diffy, minx, miny)


while True:
    (diffx, diffy, _, _) = DiffsAndMins(next)
    xes = map(lambda x: x[0], next)
    cnts = Counter(xes)
    common = cnts.most_common(1)[0][1]

    if predDiffy < diffy:
        break

    predDiffy = diffy
    prev = next
    next = list(map(increment, next))
    seconds += 1

seconds -= 1


def printm(lst, f):
    for line in lst:
        s = reduce(lambda x, y: x+f(y), line, "")
        print(s)


def printmessage(prev):
    (diffx, diffy, minx, miny) = DiffsAndMins(prev)

    area = []
    for index in range(diffy+1):
        area.append([' ' for i in range(diffx+1)])
    for p in prev:
        area[p[1]-miny][p[0]-minx] = '#'

    printm(area, lambda x: x)


printmessage(prev)
# EHAZPZHP
print("Seconds", seconds)
# 10136

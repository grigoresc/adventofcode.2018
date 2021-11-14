from functools import reduce
import re
from typing import Counter

inp = [line.strip() for line in open("sample.txt", 'r')]
inp = [line.strip() for line in open("input.txt", 'r')]


def parse(line):
    (v, x, y, z) = re.findall(r'-?\d+', line)
    return int(v), int(x), int(y), int(z)


points = list(map(parse, inp))


def printm(lst, f):
    for line in lst:
        s = reduce(lambda x, y: x+f(y), line, "")
        print(s)


def increment(item):
    return (item[0]+item[2], item[1]+item[3], item[2], item[3])


def printmessage(next):
    miny = min(next, key=lambda x: x[1])[1]
    maxy = max(next, key=lambda x: x[1])[1]
    diffy = maxy-miny
    minx = min(next, key=lambda x: x[0])[0]
    maxx = max(next, key=lambda x: x[0])[0]
    diffx = maxx-minx

    area = []
    for line in range(0, diffy):
        area.append([0 for i in range(0, diffx)])

    printm(area, lambda x: chr(ord('A')+x[0]) if x[0] != None else '#')


next = points.copy()
prediffy = 10000000
for i in range(0, 1111110):
    miny = min(next, key=lambda x: x[1])[1]
    maxy = max(next, key=lambda x: x[1])[1]
    diffy = maxy-miny
    minx = min(next, key=lambda x: x[0])[0]
    maxx = max(next, key=lambda x: x[0])[0]
    diffx = maxx-minx
    xes = map(lambda x: x[0], next)
    cnts = Counter(xes)
    common = cnts.most_common(1)[0][1]

    # print(cnts)
    print(diffx, diffy, common)
    if prediffy < diffy:
        print(prev)
        printmessage(prev)
        break
    else:
        prediffy = diffy
    # if diffy+1 == 8:
    # break
    prev = next
    next = list(map(increment, next))

miny = min(prev, key=lambda x: x[1])[1]
maxy = max(prev, key=lambda x: x[1])[1]
diffy = maxy-miny
minx = min(prev, key=lambda x: x[0])[0]
maxx = max(prev, key=lambda x: x[0])[0]
diffx = maxx-minx

area = []
for line in range(0, diffy+1):
    area.append([' ' for i in range(0, diffx+1)])
for p in prev:
    area[p[1]-miny][p[0]-minx] = '#'

printm(area, lambda x: x)
# EHAZPZHP

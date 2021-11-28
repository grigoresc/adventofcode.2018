import collections
import re
from functools import reduce

inp = [line.strip() for line in open("input.txt", 'r')]


def parse(line):
    (x, y, z, t) = re.findall(r'-?\d+', line)
    return (int(x), int(y), int(z), int(t))


points = set(map(parse, inp))


def areNear(p1, p2):
    dist = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])+abs(p1[3]-p2[3])
    return dist <= 3


def sameConstellation(c1, c2):
    for pc1 in c1:
        for pc2 in c2:
            if areNear(pc1, pc2):
                return True
    return False


def mergeConstellations(lst, c2):
    merged = False
    newlst = []
    for c1 in lst:
        if sameConstellation(c1, c2) and not merged:
            newlst.append(set.union(c1, c2))
            merged = True
        else:
            newlst.append(c1)
    if not merged:
        newlst.append(c2)
    return newlst


constellations = map(lambda x: {x}, list(points))

clen = 0

while True:
    constellations = reduce(mergeConstellations, constellations, [])
    if len(constellations) == clen:
        # no other merges..
        break
    clen = len(constellations)
print(clen)
# 422

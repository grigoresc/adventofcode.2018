
txt = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

with open('input.txt', 'r') as f:
    txt = f.readline()
inp = [int(n) for n in txt.split(' ')]


def resolveNode():
    global pos, checksum
    childs = inp[pos]
    meta = inp[pos+1]
    pos += 2
    childsval = []
    for c in range(0, childs):
        val = resolveNode()
        childsval.append(val)
    metas = []
    for m in range(0, meta):
        checksum += inp[pos]
        metas.append(inp[pos])
        pos += 1
    if childs == 0:
        return sum(metas)
    else:
        return sum(map(lambda x: childsval[x-1] if x <= len(childsval) else 0, metas))


checksum = 0
pos = 0
rootvalue = resolveNode()
print(checksum)
# 37262
print(rootvalue)
# 20839

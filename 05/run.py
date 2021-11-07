inp = """dabAcCaCBAcCcaDA"""

with open('input.txt', 'r') as f:
    inp = f.readline()


def removePolymers(inp):
    r = ""
    for c in inp:
        # print(c)
        last = r[-1:]
        if (c.islower() and last.isupper() or c.isupper() and last.islower()) and c.lower() == last.lower():
            # print("remove", c, last)
            r = r[:-1]
            continue
        r += c
    return r


r = removePolymers(inp)
print(len(r))
# 0348


def removeUnit(u):
    for c in inp:
        if c.lower() == u:
            continue
        yield c


m = 1000000
for uc in range(ord('a'), ord('z')):
    u = chr(uc)
    r = removeUnit(u)
    r = removePolymers(r)
    l = len(r)
    if l < m:
        m = l
    # print(u, r, l)
print(m)
# 4996

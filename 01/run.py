import itertools
# l = [+3, +3, +4, -2, -4]

l = [int(line.strip()) for line in open("input.txt", 'r')]
print(l)

sln1 = sum(l)
print(sln1)

c = itertools.cycle(l)

a = 0
s = []
for x in c:
    a += x
    if a in s:
        print(a)
        break
    else:
        s.append(a)
        print(a)

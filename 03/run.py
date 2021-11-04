import re
inp = ["#1 @ 1,3: 4x4",
       "#2 @ 3,1: 4x4",
       "#3 @ 5,5: 2x2"]
inp = [line.strip() for line in open("input.txt", 'r')]

leng = 2000
a = [[0 for i in range(leng)] for j in range(leng)]
la = [[0 for i in range(leng)] for j in range(leng)]

untouched = set()


def fill(no, l, t, w, h):
    untouched.add(no)
    for i in range(l, l+w):
        for j in range(t, t+h):
            a[j][i] += 1
            if la[j][i] > 0:
                if la[j][i] in untouched:
                    untouched.remove(la[j][i])
                if no in untouched:
                    untouched.remove(no)
            la[j][i] = no


for line in inp:
    (no, l, t, w, h) = map(int, re.findall(r'\d+', line))
    fill(no, l, t, w, h)

cnt = 0
for line in a:
    cnt += len(list(filter(lambda x: x > 1, line)))

print(cnt)
# 116489
print(untouched)
# 1260

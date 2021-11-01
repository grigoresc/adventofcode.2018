import itertools
l = ["bababc","abbcde"]
l = [line.strip() for line in open("input.txt", 'r')]
# print(l)
def cnt1(line):
    d=dict()
    for c in line:
        if not c in d:
            d[c]=0
        d[c]+=1
    c2 = 1 if 2 in d.values() else 0
    c3 = 1 if 3 in d.values() else 0
    return (c2,c3)
from functools import reduce

sln1=reduce(lambda a,b:(a[0]+b[0],a[1]+b[1]),map(cnt1,l),(0,0))
sln1
print(sln1[0]*sln1[1])
#5456

l = ["abcde",
"fghij",
"klmno",
"pqrst",
"fguij",
"axcye",
"wvxyz"]

l = [line.strip() for line in open("input.txt", 'r')]
def common(line1,line2):
    s=""
    for el in zip(line1,line2):
        s+=el[0] if el[0]==el[1] else ""
    return s

c=itertools.combinations(l,2)
# list(c)
m=map(lambda x:common(x[0],x[1]),c)
# list(m)
f=filter(lambda x:len(x)==len(l[0])-1,m)
print(list(f))
# megsdlpulxvinkatfoyzxcbvq

import re

txt = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

inp = [line.strip() for line in txt.split('\n')]
inp = [line.strip() for line in open("input.txt", 'r')]
inp.sort()


def parse(line):
    g = None
    if line.find("Guard") > 0:
        (y, mo, d, h, mi, g) = map(int, re.findall(r'\d+', line))
    else:
        (y, mo, d, h, mi) = map(int, re.findall(r'\d+', line))

    if h == 23:
        h = 0
        mi = 0
        if d in (28, 29) and mo == 2:
            d = 1
            mo = 3
        elif d == 30 and mo in (4, 6, 9, 11):
            d = 1
            mo += 1
        elif d == 31 and mo in (1, 3, 5, 7, 8, 10, 12):
            d = 1
            mo += 1
            mo = mo % 12
        else:
            d += 1

    date = ""+str(mo)+"-"+str(d)
    if not date in rec:
        rec[date] = {
            "lines": [],
            "mins": [0 for i in range(0, 60)]
        }

    if not g is None:
        rec[date]["guard"] = g

    if line.find("falls") > 0:
        for i in range(mi, 60):
            if rec[date]["mins"][i] == 1:
                break
            else:
                rec[date]["mins"][i] = 1
    if line.find("wakes") > 0:
        for i in range(mi, 60):
            if rec[date]["mins"][i] == 0:
                break
            else:
                rec[date]["mins"][i] = 0


rec = dict()
for line in inp:
    parse(line)

guards = set(map(lambda x: x["guard"], rec.values()))
# print(guards)


def totalMinutes(g):
    days = list(map(lambda x: x['mins'], filter(
        lambda x: x["guard"] == g, rec.values())))
    s = sum(map(sum, days))
    return s


maxv = max(map(lambda g: totalMinutes(g), guards))
maxg = next(filter(lambda g: totalMinutes(g) == maxv, guards))
# print(maxg)


def sumsPerMinute(g):
    days = list(map(lambda x: x['mins'], filter(
        lambda x: x["guard"] == g, rec.values())))
    sumhrs = [0 for i in range(0, 60)]
    for day in days:
        sumhrs = zip(sumhrs, day)
        sumhrs = list(map(lambda x: x[0]+x[1], sumhrs))
    return sumhrs


sums = sumsPerMinute(maxg)
maxv = 0
for i, c in enumerate(sums):
    if c > maxv:
        maxv = c
        maxi = i

# print(maxv, maxi)

sln1 = maxi * maxg
print(sln1)
# 94542

maxv = 0
for g in guards:
    sums = sumsPerMinute(g)
    for i, c in enumerate(sums):
        if c > maxv:
            maxv = c
            maxh = i
            maxg = g
# print(maxv, maxh, maxg)
sln2 = maxh*maxg
print(sln2)
# 50966

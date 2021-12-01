import re

txt = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

# inp = [line.strip() for line in txt.split('\n')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse(line):
    [(start, end)] = re.findall(
        r"Step (.) must be finished before step (.) can begin\.", line)
    return (start, end)


steps = list(map(parse, inp))


def buildDefs(steps):
    deps = dict()
    for step in steps:
        if step[1] not in deps.keys():
            deps[step[1]] = set()
        deps[step[1]].add(step[0])
        if step[0] not in deps.keys():
            deps[step[0]] = set()
    return deps


def Part1(steps):
    deps = buildDefs(steps)

    sln1 = ""
    while True:
        nexts = filter(lambda x: len(x[1]) == 0, deps.items())
        nexts = sorted(nexts)
        if len(nexts) == 0:
            break
        c = nexts[0][0]
        sln1 += c
        for dep in deps.keys():
            if c in deps[dep]:
                deps[dep].remove(c)
        deps.pop(c)

    return sln1


sln1 = Part1(steps)
print(sln1)


def Part2(steps):
    deps = buildDefs(steps)
    no = 5
    extraduration = 60
    workers = [0 for w in range(0, no)]
    pending = ['' for w in range(0, no)]
    time = 0
    while True:
        for idx in range(0, len(workers)):
            if workers[idx] == 1:
                c = pending[idx]
                for dep in deps.keys():
                    if c in deps[dep]:
                        deps[dep].remove(c)
            if workers[idx] > 0:
                workers[idx] -= 1

        nexts = filter(lambda x: len(x[1]) == 0, deps.items())
        nexts = sorted(nexts)
        for idx2 in range(0, len(workers)):
            if workers[idx2] > 0:
                continue

            if len(nexts) == 0:
                break

            c = nexts[0][0]
            rem = deps.pop(c)

            duration = extraduration + ord(c) - ord('A') + 1
            workers[idx2] = duration
            pending[idx2] = c
            nexts.pop(0)

        working = list(filter(lambda x: x > 0, workers))

        if len(working) == 0:
            break
        time += 1
    return time


time = Part2(steps)
print(time)
# 936

from collections import deque

marbles = deque()


def add(newM):
    global marbles
    marbles.rotate(-2)
    marbles.appendleft(newM)


def remove():
    global marbles
    marbles.rotate(7)
    return marbles.popleft()


def solve(playersno, marblesno):
    global marbles
    marbles = deque()
    marbles.append(0)

    currentPlayer = 1
    playerscores = [0 for i in range(0, playersno)]
    for m in range(1, marblesno+1):
        if m % 23 == 0:
            playerscores[currentPlayer] += m
            removed = remove()
            playerscores[currentPlayer] += removed
        else:
            add(m)

        currentPlayer += 1
        currentPlayer = currentPlayer % playersno
    sln = max(playerscores)
    print(sln)
    return sln


# samples
assert solve(9, 25) == 32

assert solve(10, 1618) == 8317
assert solve(13, 7999) == 146373
assert solve(17, 1104) == 2764
assert solve(21, 6111) == 54718
assert solve(30, 5807) == 37305
# input part 1
assert solve(459, 72103) == 388131
# input part 2
assert solve(459, 72103*100) == 3239376988

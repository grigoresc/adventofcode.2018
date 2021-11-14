marbles = dict()


def insert(currentM, newM):
    global marbles
    el1M = marbles[currentM]['nextM']
    el2M = marbles[el1M]['nextM']
    marbles[newM] = {'m': newM, 'nextM': el2M, 'prevM': el1M}
    marbles[el1M]['nextM'] = newM
    marbles[el2M]['prevM'] = newM


def pop(currentM):
    global marbles
    m = marbles[currentM]['m']
    beforeM = marbles[currentM]['prevM']
    afterM = marbles[currentM]['nextM']
    marbles[beforeM]['nextM'] = marbles[afterM]['m']
    marbles[afterM]['prevM'] = marbles[beforeM]['m']
    marbles[currentM] = None
    return (m, afterM)


def printM(start):
    global marbles
    current = start
    while True:
        print(current)
        current = marbles[current]['nextM']
        if current == start:
            break


def sln2(playersno, marblesno):
    global marbles
    marbles = dict()
    marbles[0] = {'m': 0, 'nextM': 0, 'prevM': 0}

    insert(0, 1)

    current = 1
    currentPlayer = 2
    playerscores = [0 for i in range(0, playersno)]
    for m in range(2, marblesno+1):
        if m % 23 == 0:
            playerscores[currentPlayer] += m
            for i in range(0, 7):
                current = marbles[current]['prevM']

            (retdele, current) = pop(current)
            playerscores[currentPlayer] += retdele
        else:
            insert(current, m)
            current = m

        currentPlayer += 1
        currentPlayer = currentPlayer % playersno
    sln = max(playerscores)
    print(sln)
    return sln


# samples
assert sln2(9, 25) == 32
sln2(10, 1618)
sln2(13, 7999)
sln2(17, 1104)
sln2(21, 6111)
sln2(30, 5807)
# input
sln2(459, 72103)
# 388131
sln2(459, 72103*100)
# 3239376988

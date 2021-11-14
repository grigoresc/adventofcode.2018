def sln1(playersno, marblesno):
    circle = [0, 1]
    current = 1
    currentPlayer = 2
    playerscores = [0 for i in range(0, playersno)]
    for m in range(2, marblesno+1):
        if m % 23 == 0:
            playerscores[currentPlayer] += m
            delepos = current - 7

            delepos = delepos + len(circle) if delepos < 0 else delepos
            retdele = circle.pop(delepos)
            playerscores[currentPlayer] += retdele
            nextpos = delepos
            if nextpos == len(circle) - 1:
                # strange that this case is never reached..
                nextpos = 0

        else:
            nextpos = (current+2) % len(circle)
            circle.insert(nextpos, m)

        current = nextpos
        currentPlayer += 1
        currentPlayer = currentPlayer % playersno
    print(max(playerscores))


# samples
sln1(9, 25)
sln1(10, 1618)
sln1(13, 7999)
sln1(17, 1104)
sln1(21, 6111)
sln1(30, 5807)
# input
sln1(459, 72103)
# 388131

# https://www.acmicpc.net/problem/14499

import sys

n, m, x, y, k = list(map(int, sys.stdin.readline().strip().split()))

grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))

moves = list(map(int, sys.stdin.readline().strip().split()))


# 주사위 정보 담을 객체 생성 (전역 변수)
diceGoBack = [0, 0, 0]
diceLeftRight = [0, 0, 0]
diceUp = 0


def rollDice(move, x, y):
    global diceLeftRight, diceGoBack, diceUp
    # 주사위를 굴린다
    if move == 1: # 동
        temp = diceUp
        diceUp = diceLeftRight[0]
        diceLeftRight = diceLeftRight[1:] + [temp]
        diceGoBack[1] = diceLeftRight[1]

    elif move == 2: # 서
        temp = diceUp
        diceUp = diceLeftRight[2]
        diceLeftRight = [temp] + diceLeftRight[:2]
        diceGoBack[1] = diceLeftRight[1]

    elif move == 3: # 북
        temp = diceUp
        diceUp = diceGoBack[2]
        diceGoBack = [temp] + diceGoBack[:2]
        diceLeftRight[1] = diceGoBack[1]
    elif move == 4: # 남
        temp = diceUp
        diceUp = diceGoBack[0]
        diceGoBack = diceGoBack[1:] + [temp]
        diceLeftRight[1] = diceGoBack[1]


    #
    if grid[x][y] == 0:
        grid[x][y] = diceLeftRight[1]
    else:
        diceLeftRight[1], diceGoBack[1] = grid[x][y], grid[x][y]
        grid[x][y] = 0


def movePos(x, y, move):
    if move == 1: # 동
        xNext, yNext = x, y + 1
    elif move == 2: # 서
        xNext, yNext = x, y - 1
    elif move == 3: # 북
        xNext, yNext = x - 1, y
    elif move == 4: # 남
        xNext, yNext = x + 1, y

    # 유효한 이동
    if 0 <= xNext <= n - 1 and 0 <= yNext <= m - 1:
        return xNext, yNext
    # 유효하지 않은 이동
    else:
        return -1, -1


for move in moves:
    # 새로운 주사위 위치를 생성한다
    xNext, yNext = movePos(x, y, move)

    # 새로운 주사위 위치가 valid한지 확인한다. (valid 하지 않으면, continue)
    if xNext == -1 or yNext == -1:
        continue
    # 주사위를 굴리고, 바닥면을 복사해오던지 말던지
    rollDice(move, xNext, yNext)

    # print(xNext, yNext, diceLeftRight, diceGoBack, diceUp)
    # 주사위 윗면을 출력한다
    print(diceUp)

    # 주사위 위치 갱신
    x, y = xNext, yNext

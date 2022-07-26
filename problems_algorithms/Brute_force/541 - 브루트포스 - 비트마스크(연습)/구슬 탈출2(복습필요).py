# https://www.acmicpc.net/problem/13460
import sys
from collections import deque
import copy

N, M = list(map(int, sys.stdin.readline().strip().split()))

grid = []

for i in range(N):
    line = list(sys.stdin.readline().strip())
    
    # 빨간 구슬, 파란 구슬 위치 찾기 (grid 상으로는 R, B 가 위치한 칸을 . 으로 대체한다.)
    for j in range(M):
        if line[j] == "R":
            posR = (i, j)
            line[j] = "."

        if line[j] == "B":
            posB = (i, j)
            line[j] = "."
    grid.append(line)

# 기울일 수 있는 4가지 방향에 대한 리스트
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 1번 기울임으로써, 2개의 구슬을 동시에 움직이는 함수
def move(pR, pB, dir):

    xR, yR = pR[1], pR[0]
    xB, yB = pB[1], pB[0]

    isEnd = False # 성공적으로 R 만 탈출했는지 여부
    isRend = False # 일단 R이 탈출했는지 여부
    while True:
        # 기울인 방향으로 1칸씩 움직였을 때의, 각 구슬의 후보지를 계산한다.
        xRnext, yRnext = xR + dir[1], yR + dir[0]
        xBnext, yBnext = xB + dir[1], yB + dir[0]

        # 만약 R과 B가 모두 벽에 가로막힌 경우, 이동이 완료된 것이다.
        if grid[yRnext][xRnext] == "#" and grid[yBnext][xBnext] == "#":
            break

        # 빨간 구슬이 구멍에 빠지는 경우, 탐색을 종료한다.
        if grid[yRnext][xRnext] == "O":
            isRend = True
            xR, yR = 0, 0

        # 파란 구슬이 구멍에 빠지는 경우, 탐색을 무효로 한다.
        if grid[yBnext][xBnext] == "O":
            isMoved = False
            return (pR[0], pR[1]), (pB[0], pB[1]), isMoved, isEnd

        isRmovable, isBmovable = True, True
        # 벽에 가로막혔거나, R이 이미 탈출한 경우, R은 움직일 수 없다.
        if grid[yRnext][xRnext] == "#" or isRend:
            isRmovable = False
            
        # B가 벽에 가로막힌 경우, B는 움직일 수 없다
        if grid[yBnext][xBnext] == "#":
            isBmovable = False
            
        # [R & B 가 붙어있는 경우]
        # B가 dir 방향으로 1칸 움직이면 현재 R의 위치가 될 때, 
        if xBnext == xR and yBnext == yR:
            # R이 움직일 수 있으면, 다 1칸씩 움직인다.
            if isRmovable:
                xR, yR = xRnext, yRnext
                xB, yB = xBnext, yBnext
            # R이 움직일 수 없으면, 그대로 움직임을 종료한다.
            else:
                break
        
        # R이 dir 방향으로 1칸 움직이면 현재 B의 위치가 될 때, 
        if xRnext == xB and yRnext == yB:
            # B가 움직일 수 있으면, 다 1칸씩 움직인다.
            if isBmovable:
                xR, yR = xRnext, yRnext
                xB, yB = xBnext, yBnext
            # B가 움직일 수 없으면, 그대로 움직임을 종료한다.
            else:
                break

        # R과 B가 따로 떨어져 있는데, 하나만 움직일 수 있는 경우
        if isRmovable:
            xR, yR = xRnext, yRnext

        if isBmovable:
            xB, yB = xBnext, yBnext

        # 어느 것도 움직이지 못할 경우, 종료한다.
        if not isRmovable and not isBmovable:
            break
        
            
    # R이 탈출했고, B가 잘 멈췄다면, isEnd = True
    if isRend:
        isEnd = True

    # 2개의 구슬 중 하나라도 움직였는지를 판단해서 리턴한다.
    if xR == pR[1] and yR == pR[0] and xB == pB[1] and yB == pB[0]:
        isMoved = False
    else:
        isMoved = True

    return (yR, xR), (yB, xB), isMoved, isEnd


q = deque()
qNext = deque()

q.append((posR, posB))
cnt = 0


while True:
    # print("cnt:", cnt)
    while q:

        pR, pB = q.popleft()

        for dir in dirs:
            pRnext, pBnext, isMoved, isEnd = move(pR, pB, dir)

            # 구슬이 하나라도 움직였으면, 다음 탐색 대상에 넣는다.
            if isMoved:
                qNext.append((pRnext, pBnext))

            # R이 탈출했으면, 최소 기울임 횟수 출력하고 종료한다.
            if isEnd:
                print(cnt + 1)
                exit()

            # 하나라도 움직였으면, 전/후 출력하기
            # if isMoved:
            #     gridCopy = copy.deepcopy(grid)
            #     gridCopy[pR[0]][pR[1]] = "R"
            #     gridCopy[pB[0]][pB[1]] = "B"

            #     gridCopy[pRnext[0]][pRnext[1]] = "r"
            #     gridCopy[pBnext[0]][pBnext[1]] = "b"
            #     print("R:", pR, "B:", pB, "-->", "R:", pRnext, "B:", pBnext)
            #     for row in gridCopy:
            #         print(row)

            #     print()


    q = copy.deepcopy(qNext)
    qNext = deque()
    cnt += 1


    # 만약 10번 이내로 해결안되는 문제면, 탐색을 종료한다.
    if cnt >= 10:
        break

# 탈출을 못하고 탐색이 끝난 경우, 해결이 불가능한 문제이다.
print(-1)



# https://www.acmicpc.net/problem/13460
import sys
from collections import deque
import copy

N, M = list(map(int, sys.stdin.readline().strip().split()))

grid = []

for i in range(N):
    line = list(sys.stdin.readline().strip())
    
    # 빨간 구슬, 파란 구슬 위치 찾기
    for j in range(M):
        if line[j] == "R":
            posR = (i, j)
            line[j] = "."

        if line[j] == "B":
            posB = (i, j)
            line[j] = "."
    grid.append(line)

print(posR, posB)
# 기울일 수 있는 4가지 방향에 대한 리스트
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 1번 기울임으로써, 2개의 구슬을 동시에 움직이는 함수
def move(posR, posB, dir):

    xR, yR = posR[1], posR[0]
    xB, yB = posB[1], posB[0]

    isEnd = False
    while True:
        # 기울인 방향으로 1칸씩 움직였을 때의, 각 구슬의 후보지를 계산한다.
        xRnext, yRnext = xR + dir[1], yR + dir[0]
        xBnext, yBnext = xB + dir[1], yB + dir[0]

        # 만약 후보지 전부에 .이 없을 경우, 이동이 완료된 것이다.
        if grid[yRnext][xRnext] != "." and grid[yBnext][xBnext] != ".":
            break
        # 빨간 구슬이 구멍에 빠지는 경우, 탐색을 종료한다.
        if grid[yRnext][xRnext] == "O":
            isEnd = True
            break
        # 파란 구슬이 구멍에 빠지는 경우, 탐색을 무효로 한다.
        if grid[yBnext][xBnext] == "O":
            isMoved = False
            return (posR[0], posR[1]), (posB[0], posB[1]), isMoved, isEnd

        # 여기서부턴 하나의 구슬이라도 이동이 가능한 경우
        # 벽에 막힌 경우, 움직이기 전의 좌표를 그대로 유지한다.

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if grid[yRnext][xRnext] == "#":
            xRnext, yRnext = xR, yR
            if yRnext == yB and xRnext == xB:
                break
        if grid[yBnext][xBnext] == "#":
            xBnext, yBnext = xB, yB
            if yRnext == yB and xRnext == xB:
                break
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # 현재 구슬들의 위치를 다음 루프로 넘겨준다.
        xR, yR = xRnext, yRnext
        xB, yB = xBnext, yBnext

    # 2개의 구슬 중 하나라도 움직였는지를 판단해서 리턴한다.
    if xR == posR[1] and yR == posR[0] and xB == posB[1] and yB == posB[0]:
        isMoved = False
    else:
        isMoved = True

    return (yR, xR), (yB, xB), isMoved, isEnd


q = deque()
qNext = deque()

q.append((posR, posB))
cnt = 0

while True:
    while q:

        pR, pB = q.popleft()

        for dir in dirs:
            pRnext, pBnext, isMoved, isEnd = move(pR, pB, dir)
            # 구슬이 하나라도 움직였으면, 다음 탐색 대상에 넣는다.
            if isMoved:
                qNext.append((pRnext, pBnext))

            if isEnd:
                print(cnt + 1)
                exit()

        # 전/후 출력하기
        gridCopy = copy.deepcopy(grid)
        gridCopy[pR[0]][pR[1]] = "R"
        gridCopy[pB[0]][pB[1]] = "B"

        gridCopy[pRnext[0]][pRnext[1]] = "r"
        gridCopy[pBnext[0]][pBnext[1]] = "b"
        print(pR, pB, "-->", pRnext, pBnext)
        for row in gridCopy:
            print(row)

        print()

    q = copy.deepcopy(qNext)
    qNext = deque()
    cnt += 1


    # 만약 10번 이내로 해결안되는 문제면, -1을 출력하고 종료한다.
    if cnt > 10:
        print(-1)
        exit()



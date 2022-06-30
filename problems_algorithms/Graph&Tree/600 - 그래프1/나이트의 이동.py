# https://www.acmicpc.net/problem/7562
import sys
from collections import deque

t = int(sys.stdin.readline().strip())

steps = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

for _ in range(t):
    l = int(sys.stdin.readline().strip())

    rStart, cStart = list(map(int, sys.stdin.readline().strip().split()))
    rEnd, cEnd = list(map(int, sys.stdin.readline().strip().split()))

    board = [[-1]*l for _ in range(l)]

    q = deque()
    q.append((rStart, cStart))

    # 시작칸은 한 번도 이동하지 않아도 도달하는 칸이므로, 0 값을 기록한다.
    board[rStart][cStart] = 0

    while q:
        rNow, cNow = q.popleft()
        # 현재 탐색의 중심이 되는 칸이 목표칸이면, 최소 이동 횟수를 출력하고 탐색을 종료한다.
        if rNow == rEnd and cNow == cEnd:
            print(board[rNow][cNow])
            break

        for step in steps:
            r, c = rNow + step[0], cNow + step[1]

            # 좌표가 범위를 넘어설 경우, skip 한다.
            if r < 0 or r >= l or c < 0 or c >= l:
                continue

            if board[r][c] == -1:
                board[r][c] = board[rNow][cNow] + 1
                q.append((r, c))






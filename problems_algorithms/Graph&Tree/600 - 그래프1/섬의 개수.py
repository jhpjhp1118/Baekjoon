# https://www.acmicpc.net/problem/4963
import sys
from collections import deque
# <단지번호 붙이기> 와 매우 유사한 문제!

steps = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

while True:
    w, h = list(map(int, sys.stdin.readline().strip().split()))

    # 0 0 이면, 프로그램 종료한다.
    if w == 0 and h == 0:
        exit()

    data = []
    for _ in range(h):
        data.append(list(map(int, sys.stdin.readline().strip().split())))

    visited = [False]*(w*h)

    islands = []


    q = deque([])
    for i in range(w*h):

        row, col = i//w, i%w
        if data[row][col] == 0:
            visited[i] = True
            continue

        island = []

        if not visited[i]:
            q.append(i)
            visited[i] = True
            island.append(i)

        while q:
            now = q.popleft()
            row, col = now//w, now%w
            for step in steps:
                r, c = row + step[0], col + step[1]
                target = r*w + c
                if 0 <= r < h and 0 <= c < w and not visited[target]:
                    visited[target] = True

                    if data[r][c] == 1:
                        q.append(target)
                        island.append(target)

        if island:
            islands.append(island)

    print(len(islands))
# https://www.acmicpc.net/problem/6087
import sys
from collections import deque
input = sys.stdin.readline

"""
아이디어: 거울 beam을 벽에 닿거나 or grid 범위를 넘어갈 때까지 쭉 쏘면서, 탐색한다.
"""

w, h = list(map(int, input().strip().split()))

grid = []
razor = []
for i in range(h):
    line = list(input().strip())
    for j in range(w):
        if line[j] == "C":
            razor.append((i, j))

    grid.append(line)

# 레이저 통신의 출발지 & 도착지 설정
start = razor[0]
end = razor[1]

q = deque()
q.append(start)

# 방문 여부 & 해당 칸에 도달하기 위한 최소 거울 갯수를 기록하는 grid 생성
visited = [[100000]*w for _ in range(h)] # w, h <= 100 이므로, 적당히 큰 수로 초기화
visited[start[0]][start[1]] = -1

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while q:
    r, c = q.popleft()
    # 종료칸에 도달한 경우, 최소 거울 갯수를 출력하고 종료한다.
    if (r, c) == end:
        print(visited[r][c])
        exit()

    # 상하좌우로 거울 beam을 쏜다.
    for step in steps:
        nr, nc = r + step[0], c + step[1]

        # 거울 beam을 쏘기 위해, while loop를 사용한다.
        while True:
            # grid 범위를 벗어날 경우, 거울 beam을 종료한다.
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                break
            # 벽에 닿을 경우, 거울 beam을 종료한다.
            if grid[nr][nc] == "*":
                break
            # 해당 칸을 가는데 필요했던 거울 갯수보다, 현재 탐색 기준 필요한 거울 갯수가 많다면, 거울 beam을 종료한다.
            if visited[nr][nc] < visited[r][c] + 1:
                break

            q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
            # 진행했던 방향으로 1칸 더 진행한다.
            nr += step[0]
            nc += step[1]

# https://www.acmicpc.net/problem/3055
import sys
from collections import deque
input = sys.stdin.readline

R, C = list(map(int, input().strip().split()))

grid = []
water = [] # 물이 퍼져나갈 seed 를 기록할 변수
cave = (-1, -1) # 동굴 위치 (도착지)
start = (-1, -1) # 고슴도치 위치 (출발지)

for i in range(R):
    line = list(input().strip())
    grid.append(line)
    # 물 seed, 고슴도치 위치, 동굴 위치 찾아놓기
    for j in range(C):
        if line[j] == "*":
            water.append((i, j))

        elif line[j] == "S":
            start = (i, j)

        elif line[j] == "D":
            cave = (i, j)

visited = [[-1] * C for _ in range(R)]

water = deque(water)

q = deque()
q.append(start)

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    # 물을 퍼져나가게 한다.
    for _ in range(len(water)):
        rw, cw = water.popleft()

        for step in steps:
            rws, cws = rw + step[0], cw + step[1]

            if rws < 0 or rws >= R or cws < 0 or cws >= C or grid[rws][cws] == "*" or grid[rws][cws] == "X":
                continue

            grid[rws][cws] = "*"
            water.append((rws, cws))

    # 고슴도치를 이동시킨다.
    for _ in range(len(q)):
        rh, ch = q.popleft()

        for step in steps:
            rhs, chs = rh + step[0], ch + step[1]

            if rhs < 0 or rhs >= R or chs < 0 or chs >= C or grid[rhs][chs] == "X" or visited[rhs][chs] != -1:
                continue

            grid[rhs][chs] = "*"
            water.append((rhs, chs))
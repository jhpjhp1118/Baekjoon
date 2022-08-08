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
    # 물 seed, 고슴도치 시작 위치, 동굴 위치 찾아놓기
    for j in range(C):
        if line[j] == "*": # 물 seed
            water.append((i, j))

        elif line[j] == "S": # 고슴도치 시작 위치
            start = (i, j)

        elif line[j] == "D": # 동굴 위치
            cave = (i, j)

# 방문 여부 확인 & 해당 칸에 고슴도치가 도달하기 위한 최소 이동 횟수를 기록하는 grid 생성
visited = [[-1] * C for _ in range(R)]

water = deque(water)

q = deque()
q.append(start)

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0
while q:
    # 1) 물을 먼저 퍼져나가게 한다.
    for _ in range(len(water)):
        rw, cw = water.popleft()

        for step in steps:
            rws, cws = rw + step[0], cw + step[1]
            # 후보칸이 grid를 벗어나거나, 이미 물이 차있거나, 벽이거나, 동굴이면, skip 한다.
            if rws < 0 or rws >= R or cws < 0 or cws >= C or grid[rws][cws] == "*" \
                or grid[rws][cws] == "X" or grid[rws][cws] == "D":
                continue
            
            # 후보칸에 물을 채운다.
            grid[rws][cws] = "*"
            water.append((rws, cws))

    # 2) 고슴도치를 이동시킨다.
    for _ in range(len(q)):
        rh, ch = q.popleft()
        # 동굴에 도착하면, 최소 이동 횟수를 출력하고, 종료한다.
        if (rh, ch) == cave:
            print(visited[rh][ch])
            exit()

        for step in steps:
            rhs, chs = rh + step[0], ch + step[1]
            # 후보칸이 grid를 벗어나거나, 벽이거나, 물이거나, 방문했던 칸이면, skip 한다.
            if rhs < 0 or rhs >= R or chs < 0 or chs >= C or grid[rhs][chs] == "X" or \
                grid[rhs][chs] == "*" or visited[rhs][chs] != -1:
                continue

            visited[rhs][chs] = cnt + 1
            q.append((rhs, chs))

    cnt += 1

# 고슴도치가 굴로 이동하지 못하고 탐색이 종료되었을 경우, KAKTUS를 출력한다.
print("KAKTUS")

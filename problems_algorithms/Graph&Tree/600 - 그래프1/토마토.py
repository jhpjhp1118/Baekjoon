# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
import copy

m, n = list(map(int, sys.stdin.readline().strip().split()))

data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [False]*(n*m)

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# 핵심 아이디어: bfs로 탐색하면서, queue가 다 끝난 뒤, 0 이 아직도 존재하면 -1 출력, 존재하지 않으면 그 최소 일수 출력
qNow = deque()
qNext = deque()

# 전체 성분들을 다 확인해서, 모든 1을 queue에 추가한다.
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            qNow.append(i*m + j)

day = 0
while True:
    while qNow:
        now = qNow.popleft()
        row, col = now//m, now%m
        for step in steps:
            r, c = row + step[0], col + step[1]
            # 좌표가 범위를 벗어나면, skip한다.
            if r < 0 or r >= n or c < 0 or c >= m:
                continue
            # 토마토가 이미 익었거나, 없는 좌표면 skip한다.
            if data[r][c] == 1 or data[r][c] == -1:
                continue
            else:
                target = r * m + c
                qNext.append(target)
                data[r][c] = 1


    # 다음날에 탐색할 토마토가 없다면, 탐색을 종료한다.
    if len(qNext) == 0:
        break

    day += 1
    # 그냥 얕은 복사를 하면, qNext와 qNow의 변화가 동기화되어 버리므로, 깊은 복사를 해서 성분만 복사한다.
    qNow = copy.deepcopy(qNext)
    qNext = deque()
    # print(qNow, qNext)
    # for row in data:
    #     print(row)

# 만약 탐색이 끝났는데도 안 익은 토마토가 있다면, -1을 출력한다.
for row in data:
    if 0 in row:
        print(-1)
        exit()

print(day)



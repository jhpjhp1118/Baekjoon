# https://www.acmicpc.net/problem/1261
import sys
from collections import deque
import copy

"""
아이디어: 특정 칸까지 가는데 있어서, 파괴해야하는 최소한의 벽의 갯수를 bfs 탐색해가며 기록해나간다.
"""

m, n = list(map(int, sys.stdin.readline().strip().split()))

maze = []
for _ in range(n):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# 최소 파괴 횟수를 기록하는 grid를 생성한다. 아직 한번도 안 가본 곳은 -1로 설정한다.
visited = [[-1]*m for _ in range(n)]
visited[0][0] = 0 # 시작 위치는 0으로 초기화한다.

q = deque()
q.append((0, 0)) 
qNext = deque()

# 처음 위치와 목표지가 동일한 경우
if n == 1 and m == 1:
    print(0)
    exit()

while q: # 다음으로 탐색할 q가 아예 남지 않았을 경우, 탐색을 종료한다.
    while q: # 당장의 q의 성분이 사라질 때까지 탐색한다.
        r, c = q.popleft()

        for step in steps:
            rt, ct = r + step[0], c + step[1]
            # 범위를 벗어나는 경우, skip 한다.
            if rt < 0 or rt >= n or ct < 0 or ct >= m:
                continue

            # 아직 한번도 안 가본 곳일 경우
            if visited[rt][ct] == -1:
                # 벽이 있을 경우, 현재 위치에서의 최소 파괴 횟수 + 1 을 기록한다.
                if maze[rt][ct] == 1:
                    visited[rt][ct] = visited[r][c] + 1
                # 벽이 없을 경우, 현재 위치에서의 최소 파괴 횟수를 그대로 기록한다.
                else:
                    visited[rt][ct] = visited[r][c]
                # 다음의 탐색 대상으로 추가한다.
                qNext.append((rt, ct))
            # 한번이라도 가본 곳일 경우
            else:
                # 벽의 유무에 따라 비교값을 계산한다.
                if maze[rt][ct] == 1: # 벽이 있을 경우
                    compare = visited[r][c] + 1
                else: # 벽이 없을 경우
                    compare = visited[r][c]

                # 기존의 최소 파괴 횟수가 비교값 이하일 경우, 아무런 변화 없다.
                if visited[rt][ct] <= compare:
                    continue
                # 비교값이 새로운 최소값일 경우, 그 비교값으로 갱신하고, 다음의 탐색 대상으로 추가한다.
                else:
                    visited[rt][ct] = compare
                    qNext.append((rt, ct))

    # 다음의 탐색 대상을 q에 복사한다.
    q = copy.deepcopy(qNext)
    # qNext를 빈 deque로 만든다.
    qNext = deque()

print(visited[n - 1][m - 1])






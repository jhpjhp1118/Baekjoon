# https://www.acmicpc.net/problem/2178
import sys
from collections import deque

# 핵심: bfs로 하는 것이, 더 쉽게 계산효율적으로 코드를 짤 수 있다!

n, m = list(map(int, sys.stdin.readline().strip().split()))

maze = []
for _ in range(n):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def bfs(rStart, cStart):
    q = deque([(rStart, cStart)])

    while q:
        rNow, cNow = q.popleft()
        for step in steps:
            r, c = rNow + step[0], cNow + step[1]

            # 좌표계 범위를 넘어가면, skip 한다.
            if r < 0 or r >= n or c < 0 or c >= m:
                continue
            # 갈 수 없는 칸이면, skip 한다.
            if maze[r][c] == 0:
                continue
            # 갈 수 있는 칸이면, 그 칸까지 가는 최소 경로 칸 수를 기록해나간다. (동적 프로그래밍과 비슷함)
            # 맨 첫번째 칸은, 3이 기록되게 된다. 한번 갔다오기 때문이라 비효율적인 코드지만, 사소한 부분이라 무시한다.
            if maze[r][c] == 1:
                maze[r][c] = maze[rNow][cNow] + 1
                q.append((r, c))

    return maze[n-1][m-1]


print(bfs(0, 0))



# https://www.acmicpc.net/problem/16946
import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

grid = []
wall = [] # 벽 칸들의 좌표를 저장할 리스트 생성
movable = []
ans = [[0] * m for _ in range(n)] # 답을 기록할 grid 생성
for i in range(n):
    line = list(map(int, list(input().strip())))
    grid.append(line)
    # 벽 칸의 좌표들 미리 찾아놓기
    for j in range(m):
        if line[j] == 1:
            wall.append((i, j))
        else:
            movable.append((i, j))

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def check(grid, p):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((p[0], p[1]))
    visited[p[0]][p[1]] = 1

    cnt = 1
    while q:

        nr, nc = q.popleft()
        for step in steps:
            r, c = nr + step[0], nc + step[1]
            # grid 범위를 벗어날 경우, skip 한다.
            if r < 0 or r >= n or c < 0 or c >= m:
                continue

            if grid[r][c] == 0 and visited[r][c] == 0:
                cnt += 1
                q.append((r, c))
                visited[r][c] = 1

    return cnt

gridCnt = [[0] * m for _ in range(n)]
for p in movable:
    gridCnt = check(grid, p)

for w in wall:
    val = 0
    for step in steps:
        val += gridCnt[w[0] + step[0]][w[1] + step[1]]
    ans[w[0]][w[1]] = val

for row in ans:
    print("".join(list(map(str, row)))) # !!숫자로 된 리스트를 여백없이 출력하는 명령어!!

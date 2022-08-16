# https://www.acmicpc.net/problem/10026
import sys
from collections import deque
input = sys.stdin.readline

"""
아이디어: 적록색약이 아닐 경우 먼저 count 한다 --> G를 R로 바꿔준다 --> 적록색약일 경우를 count 한다.
주의) 시간초과 문제를 해결하는 2가지 방법
1. dfs를 사용한다.
2. bfs를 사용하되, visited[r][c] = True로 만들어주는 타이밍을 잘 고려한다.
"""

n = int(input().strip())

grid = []
for _ in range(n):
    line = list(input().strip())
    grid.append(line)
# 초기화
normal_count, ill_count = 0, 0

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(i, j, visited, grid):

    q = deque()
    q.append((i, j))
    color = grid[i][j]
    visited[i][j] = True # [효율성!] 만약 q.popleft() 직후에 visited[r][c] = True 해주면, 중복해서 탐색하는 visited의 횟수가 많아진다.
    while q:
        r, c = q.popleft()
        # 여기서 visited[r][c] = True 해주면, 중복이 많아진다! (사실 틀린 탐색임)
        for step in steps:
            nr, nc = r + step[0], c + step[1]
            # grid를 벗어나거나, 이미 방문했거나, 현재 색깔과 다른 경우, skip 한다.
            if nr < 0 or nr >= n or nc < 0 or nc >= n or visited[nr][nc] or grid[nr][nc] != color:
                continue

            q.append((nr, nc))
            visited[nr][nc] = True # [효율성!]

visited = [[False]*n for _ in range(n)]

# 적록색약 없는 경우에 대해, 영역 갯수 찾기
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited, grid)
            normal_count += 1

# G 를 R 로 바꾸기
for i in range(n):
    for j in range(n):
        if grid[i][j] == "G":
            grid[i][j] = "R"

# 적록색약 있는 경우에 대해, 영역 갯수 찾기
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited, grid)
            ill_count += 1

print(normal_count, ill_count)


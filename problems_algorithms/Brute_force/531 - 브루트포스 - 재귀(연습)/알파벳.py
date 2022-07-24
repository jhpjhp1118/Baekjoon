# https://www.acmicpc.net/problem/1987

# 주의!) 시간 초과 안하려면, Pypy3 로 실행해야 함!!

import sys

R, C = list(map(int, sys.stdin.readline().strip().split()))

grid = []
for _ in range(R):
    grid.append(list(sys.stdin.readline().strip()))

visited = [0]*26 # 모든 알파벳에 대해, 방문했는지 기록하는 리스트
ordA = ord("A")
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

ans = -1

def dfs(row, col, cnt):
    global ans

    # 더 진행할 수 있는 방향이 남아있는지 확인한다.
    dirCurr = []
    for d in dir:
        r = row + d[0]
        c = col + d[1]
        # grid 범위를 벗어나는 경우, skip 한다.
        if r < 0 or r >= R or c < 0 or c >= C:
            continue

        # 더 진행할 수 있는 방향이 있으면, dirCurr에 append 해놓는다.
        if visited[ord(grid[r][c]) - ordA] == 0:
            dirCurr.append(d)

    # 더 진행할 곳이 없을 경우, 지금까지 온 경로의 횟수와 최대값을 비교 & 갱신해준다.
    if len(dirCurr) == 0:
        ans = max(ans, cnt)
        return

    # 더 진행할 곳이 있을 경우, 더 깊게 진행한다.
    for d in dirCurr:
        r = row + d[0]
        c = col + d[1]

        visited[ord(grid[r][c]) - ordA] = 1
        dfs(r, c, cnt + 1)
        visited[ord(grid[r][c]) - ordA] = 0


visited[ord(grid[0][0]) - ordA] = 1 # 시작점의 visited 값을 1로 기록한다.
dfs(0, 0, 1)
print(ans)


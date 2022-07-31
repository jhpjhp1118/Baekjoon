# https://www.acmicpc.net/problem/2206
import sys
from collections import deque

input = sys.stdin.readline

"""
아이디어: 벽 파괴 기회를 사용했는지 여부에 따라, 방문 여부 & 최소 이동 횟수를 기록하는 grid를 사용한다.
"""

n, m = list(map(int, input().strip().split()))

maze = []
for i in range(n):
    line = list(map(int, list(input().strip())))
    maze.append(line)

# 벽 파괴 여부에 따라 최소 이동 횟수를 기록하는 grid 생성
# 3차원: 0 --> 벽을 1번도 파괴하지 않고 갈 때의 이동 횟수 (벽 파괴 X)
#       1 --> 벽을 1번 파괴한 상태로 갈 때의 이동 횟수 (벽 파괴 O)
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

q = deque()
q.append((0, 0, 0)) # 형식: row / col / 벽 파괴 여부(boom!)

steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
while q:
    nr, nc, boom = q.popleft()

    # 도착지 칸에 도착하면, 최소 이동횟수를 출력하고 종료한다.
    if nr == n - 1 and nc == m - 1:
        print(visited[nr][nc][boom])
        exit()

    for step in steps:
        r, c = nr + step[0], nc + step[1]
        # grid 범위를 벗어날 경우, skip 한다.
        if r < 0 or r >= n or c < 0 or c >= m:
            continue
        # 타겟으로 하는 칸이 벽이고, 아직 벽 파괴 기회를 사용하지 않은 경우, 벽 파괴 기회를 사용해본다.
        if maze[r][c] == 1 and boom == 0:
            visited[r][c][1] = visited[nr][nc][0] + 1
            q.append((r, c, 1))

        # 타겟으로 하는 칸이 빈 칸이고, 아직 한번도 방문하지 않은 곳이면, 단순하게 이동한다.
        if maze[r][c] == 0 and visited[r][c][boom] == 0:
            visited[r][c][boom] = visited[nr][nc][boom] + 1
            q.append((r, c, boom))

# 해결을 못하는 미로일 경우, -1을 출력하고 종료한다.
print(-1)





# https://www.acmicpc.net/problem/16954
import sys
from collections import deque
input = sys.stdin.readline

"""
주의) 한 번 방문했던 칸도 방문해야 풀리는 경우도 있다. --> visited 는 사용하지 말아야 함!
"""

grid = []
wall = []
for i in range(8):
    line = list(input().strip())
    grid.append(line)
    # 벽 위치들 미리 찾기
    for j in range(8):
        if line[j] == "#":
            wall.append((i, j))

# 8가지 방향 정의
steps = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

q = deque()
q.append((7, 0)) # 시작 칸: 가장 왼쪽 아래 칸

# 지나간 시간이 몇 초인지 count 하기 위한 변수 생성.
cnt = 0
while q:
    for i in range(len(q)):
        r, c = q.popleft()

        # 가장 오른쪽 위 칸에 도달할 경우, 탐색을 종료한다.
        if r == 0 and c == 7:
            print(1)
            exit()
        # 현재 칸으로 벽이 밀려온 경우, skip 한다.
        if grid[r][c] == "#":
            continue

        for step in steps:
            nr, nc = r + step[0], c + step[1]
            # 후보칸이 grid를 벗어나거나, 이미 방문했을 경우, skip 한다.
            if nr < 0 or nr >= 8 or nc < 0 or nc >= 8:
                    continue
            # 벽일 경우, skip 한다.
            if grid[nr][nc] == "#":
                continue

            q.append((nr, nc))

        if r - 2 >= 0 and grid[r - 2][c] == "#":
            q.append((r, c))

    # 벽들을 한 칸 아래로 이동시킨다. (마지막 줄의 벽은 제거한다)
    for wr, wc in wall:
        grid[wr + cnt][wc] = "."
    cnt += 1
    wall = [x for x in wall if x[0] + cnt < 8] # grid 범위를 넘어선 벽은 제거한다.
    for wr, wc in wall:
        grid[wr + cnt][wc] = "#"



# 탐색이 종료된 뒤에 도달하지 못한 경우, 0을 출력한다.
print(0)


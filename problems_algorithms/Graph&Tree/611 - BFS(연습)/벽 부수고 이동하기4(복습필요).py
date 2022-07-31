# https://www.acmicpc.net/problem/16946
import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

grid = []
wall = [] # 벽 칸들의 좌표를 저장할 리스트 생성
# 방문 여부를 표시할 grid 생성. group 표시 역할도 한다.
visited = [[0] * m for _ in range(n)]

ans = [[0] * m for _ in range(n)] # 답을 기록할 grid 생성
for i in range(n):
    line = list(map(int, list(input().strip())))
    grid.append(line)
    # 벽 칸의 좌표들 미리 찾아놓기
    for j in range(m):
        if line[j] == 1:
            wall.append((i, j))

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

groupNum = 0
def fillArea(p):
    global groupNum
    # group을 구분하기 위해, groupNum을 하나 증가시켜준다.
    groupNum += 1

    visited[p[0]][p[1]] = groupNum
    # 연결된 영역의 좌표들을 담아놓을 리스트 생성
    zone = [p]

    q = deque()
    q.append(p)

    area = 1
    while q:

        nr, nc = q.popleft()
        for step in steps:
            r, c = nr + step[0], nc + step[1]
            # grid 범위를 벗어날 경우, skip 한다.
            if r < 0 or r >= n or c < 0 or c >= m:
                continue

            if grid[r][c] == 0 and visited[r][c] == 0:
                area += 1
                # 10을 넘어가면, 10으로 나눈 나머지로 바꿔준다.
                if area > 10:
                    area %= 10
                q.append((r, c))
                visited[r][c] = groupNum # group 구분해준다.
                zone.append((r, c))

    # 탐색을 종료하면, 같은 영역에 해당하는 모든 칸들에, (area 값 * (-1))을 채워넣는다.
    area = -(area % 10)
    for z in zone:
        grid[z[0]][z[1]] = area


# grid를 왼쪽 위 --> 오른쪽 아래로 훑어가면서, 0 칸의 영역 넓이를 찾은 뒤, 해당 영역의 모든 칸들이 그 영역 넓이값을 가지게 한다.
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and visited[i][j] == 0:
            fillArea((i, j))


for w in wall:
    # 벽이 있는 칸도 영역에 포함되므로, 1부터 시작한다.
    val = 1
    added = set() # 더했던 group인지 확인하기 위한 set 생성
    for step in steps:
        r, c = w[0] + step[0], w[1] + step[1]

        # grid 범위를 벗어날 경우, skip 한다.
        if r < 0 or r >= n or c < 0 or c >= m:
            continue

        # 상, 하, 좌, 우 칸들 중, 음수 값을 가지는 칸이고, 더하지 않았던 group이면, 그 절대값을 더해간다.
        if grid[r][c] < 0 and visited[r][c] not in added:
            val -= grid[r][c]
            added.add(visited[r][c]) # 더한 group이라고 기록한다.
    ans[w[0]][w[1]] = val % 10


for row in ans:
    print("".join(list(map(str, row)))) # !!숫자로 된 리스트를 여백없이 출력하는 명령어!!


"""
연습용 test case
5 5
00001
00001
00001
00110
00010
"""

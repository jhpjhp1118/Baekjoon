# https://www.acmicpc.net/problem/2146
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))


"""
아이디어:
- bfs로 모든 섬을 찾아낸다
    - 모든 칸을 돌면서, seed가 될 칸을 찾는다 (visited[i][j] == False)
    - seed로부터 퍼져나가면서, 한 섬의 모든 칸을 찾아서 추가한다. (별도의 grid or grid의 1값을 2,3,4,,,로 바꾸기)


* 외곽점들이 최단거리를 탐색하는 기준점이 된다.
    - 외곽점 기준: 상하좌우 중 하나라도 0인 칸을 가지는 non-zero 칸

* 최단거리를 어떻게 찾지?
- 외곽점들을 하나씩 탐색하면서, bfs로 해당 외곽점 <--> 가장 가까운 아무 다른 섬 사이의 거리를 찾는다
- 그 최단거리가 이전 최단거리보다 작은 경우, 갱신해준다.

주의) 링 모양으로 생긴 섬의 경우! 이것을 신경안쓰면, TypeError를 야기할 가능성이 있음!
5 
1 1 1 0 0
1 0 1 0 0
1 1 1 0 0
0 0 0 0 0
0 0 0 0 1
"""

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]
contour = []

# 섬들을 10단위로 그룹화해준다
# ex) 첫번째 섬 --> 10, 두번째 섬 --> 20 ...
def classifyIslands(row, col, island):
    q = deque()
    q.append((row, col))
    grid[row][col] = island

    while q:
        r, c = q.popleft()
        isContour = False
        for step in steps:
            rt, ct = r + step[0], c + step[1]

            if rt < 0 or rt >= n or ct < 0 or ct >= n:
                continue
            # 만약 주변에 바다가 있는 칸이면, 외곽칸으로 간주한다.
            if grid[rt][ct] == 0:
                isContour = True
            # 만약 주변에 육지칸이 있으면, 그 칸은 연결된 섬의 칸이다.
            if grid[rt][ct] == 1:
                grid[rt][ct] = island
                q.append((rt, ct))
        
        if isContour:
            contour.append((r, c))


def findMinDist(row, col, start, minDists):
    q = deque()
    q.append((row, col))

    while q:
        r, c = q.popleft()

        for step in steps:
            rt, ct = r + step[0], c + step[1]
            # grid 범위를 벗어날 경우, skip 한다.
            if rt < 0 or rt >= n or ct < 0 or ct >= n:
                continue
            # 육지면서, 시작점의 섬과 다른 섬이면, 최소거리를 반환한다.
            if grid[rt][ct] != 0 and abs(grid[rt][ct]) != start:
                return minDists[r][c]

            # 바다면서, mindists도 아직 기록되지 않은 칸이면, 이전 거리 + 1 을 기록해준다.
            if grid[rt][ct] == 0 and minDists[rt][ct] == 0:
                minDists[rt][ct] = minDists[r][c] + 1
                q.append((rt, ct))
                continue



# 섬들을 10단위로 구분해놓기
island = 10
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            classifyIslands(i, j, island)
            island += 10

# 외곽칸의 경우, 음수로 만들어서 구분해준다.
for cnt in contour:
    grid[cnt[0]][cnt[1]] *= -1

ans = 1e9
for cnt in contour:
    # minDists 그리드를 생성해준다.
    minDists = [[0] * n for _ in range(n)]

    # 해당 cnt 점 <--> 가까운 아무 다른 섬까지의 최단거리를 구해준다.
    dist = findMinDist(cnt[0], cnt[1], abs(grid[cnt[0]][cnt[1]]), minDists)

    # TypeError 방지용 조건 - 주어진 grid & 해당 cnt 점에서는 최단거리가 아예 존재하지 않을 수도 있다.
    # 최단거리가 아예 존재하지 않으면, findMinDist = None이 되므로, 이를 확인해준다.
    if dist == None:
        continue
    else:
        ans = min(ans, dist)

print(ans)




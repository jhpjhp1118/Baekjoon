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
- 외곽점들을 하나씩 탐색하면서, bfs로 해당 외곽점 <--> 가장 가까운 아무 다른 섬 사이의 거리를 기록해나간다.
- 기록해나간 거리값들 중 최소값을 찾는다.
"""

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]
contour = []

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

            if grid[rt][ct] == 0:
                isContour = True

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

            if rt < 0 or rt >= n or ct < 0 or ct >= n:
                continue

            if grid[rt][ct] == 0 and minDists[rt][ct] == 0:
                minDists[rt][ct] = minDists[r][c] + 1
                q.append((rt, ct))
                continue

            if grid[rt][ct] != 0 and abs(grid[rt][ct]) != start:
                return minDists[r][c]


# 섬들을 10단위로 구분해놓기
island = 10
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            classifyIslands(i, j, island)
            island += 10

for cnt in contour:
    grid[cnt[0]][cnt[1]] *= -1

# 확인용!
# for row in grid:
#     print(row)


ans = 1e9
for cnt in contour:
    minDists = [[0] * n for _ in range(n)]
    ans = min(ans, findMinDist(cnt[0], cnt[1], abs(grid[cnt[0]][cnt[1]]), minDists))

# for row in minDists:
#     print(row)
print(ans)




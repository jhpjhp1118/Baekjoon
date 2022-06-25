# https://www.acmicpc.net/problem/16929
import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

data = []
for _ in range(n):
    data.append(list(sys.stdin.readline().strip()))

steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 함수 정의하기
def dfs(idx, clockDir, char, prevDir):

    row, col = idx//m, idx%m

    for j in range(4):
        r, c = row + steps[j][0], col + steps[j][1]
        if r < 0 or r >= n or c < 0 or c >= m:
            continue

        target = r*m + c
        if data[r][c] == char and not visited[target]:
            visited[target] = True
            if j - prevDir == 1 or j - prevDir == 3:
                dfs(target, clockDir=clockDir+1, prevDir=j)
            else:
                dfs(target, clockDir=clockDir, prevDir=j)
            visited[target] = False # ???? 이게 맞나?

visited = [False]*(n*m)

# 아직 탐색을 한번도 안해본 칸이면, dfs 함수를 적용시켜보기
for i in range(n*m):
    if not visited[i]:
        dfs(i, clockDir=0, char=data[i//m][i%m], prevDir=100)


# https://www.acmicpc.net/problem/10971
import sys

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

global ans
ans = int(1e9)

def dfs(start, next, cost, visited):
    global ans
    if len(visited) == n:
        if data[next][start] != 0:
            ans = min(ans, cost + data[next][start])

    # 현재 비용이, 갱신중인 최소비용보다 이미 크면, dfs를 더 깊게 탐색하지 않는다.
    if cost >= ans:
        return

    for i in range(n):
        if data[next][i] != 0 and i not in visited:
            visited.append(i)
            dfs(start, i, cost + data[next][i], visited)
            visited.pop()

dfs(0, 0, 0, [0]) # 순환 경로이므로, 한 점만 확인해도 된다
print(ans)



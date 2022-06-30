# https://www.acmicpc.net/problem/13023
import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

# graph 간선 정보 읽어오기
graph = [[] for _ in range(n)]
for i in range(m):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))
    graph[p1].append(p2)
    graph[p2].append(p1)


visited = [False] * n
def dfs(idx, depth):
    # 탐색한 그래프의 현재 깊이가 5가 되면, 1을 출력하고 프로그램을 종료한다.
    if depth == 5:
        print(1)
        exit()

    for i in graph[idx]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(idx=i, depth=1)
    visited[i] = False
# 깊이가 5인 경우를 발견하지 못하면, 0을 출력한다.
print(0)


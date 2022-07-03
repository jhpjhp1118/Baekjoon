# https://www.acmicpc.net/problem/1967
import sys
from collections import deque

# "트리의 지름(1)" 과 완전 동일. (인풋 방식만 빼고 다 똑같음)

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p1, p2, w = list(map(int, sys.stdin.readline().strip().split()))

    graph[p1].append((p2, w))
    graph[p2].append((p1, w))


def bfs(start):

    visited = [-1] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = 0
    distMax, ndeMax = 0, 0

    while q:
        now = q.popleft()

        for nde, dist in graph[now]:
            if visited[nde] == -1:
                visited[nde] = visited[now] + dist
                q.append(nde)

                if visited[nde] > distMax:
                    distMax, ndeMax = visited[nde], nde

    return distMax, ndeMax

dist, nde = bfs(1)
dist, nde = bfs(nde)

print(dist)



# https://www.acmicpc.net/problem/1167
import sys
from collections import deque
"""
아이디어: 임의의 노드에서 가장 멀리있는 노드를 찾는다 --> 그 뒤 그 노드로부터 가장 멀리있는 노드와의 거리를 찾으면 된다.
핵심) 가장 멀리 떨어져있는 2개의 노드 nde1, nde2가 있다고 가정한다면,
        임의의 노드에서 가장 멀리있는 노드를 찾았을 때, 그 노드는 nde1 아니면 nde2이다.
"""
v = int(sys.stdin.readline().strip())

graph = [[] for _ in range(v + 1)]

for _ in range(v):
    s = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, len(s) - 1, 2):
        graph[s[0]].append((s[i], s[i + 1]))


def bfs(start):
    visited = [-1]*(v + 1) # start 노드로부터의 거리를 기록하는 리스트
    q = deque()
    q.append(start)
    visited[start] = 0
    distMax, ndeMax = 0, 0 # return할 최대 거리 & 해당 노드

    while q:
        now = q.popleft()
        for nde, dist in graph[now]:
            # 처음 방문하는 곳일 경우
            if visited[nde] == -1:
                # 거리를 갱신해준다.
                visited[nde] = visited[now] + dist
                # 다음 탐색 대상으로 추가한다.
                q.append(nde)
                # 거리의 최대값을 넘어서면, 갱신해준다.
                if visited[nde] > distMax:
                    distMax, ndeMax = visited[nde], nde

    return distMax, ndeMax

# 일단 무조건 존재하는 1번 노드를 임의의 노드로 사용하여, 1번 노드에서 가장 멀리있는 노드를 찾는다.
dist, nde = bfs(1)

# 1번 노드로부터 가장 멀리있는 노드 <--> 그로부터 가장 멀리있는 노드 사이의 거리를 구한다.
dist, nde = bfs(nde)
print(dist)


# https://www.acmicpc.net/problem/1260
# BFS 설명링크: https://freedeveloper.tistory.com/373
# 참고링크: https://devchopin.com/blog/96/

import sys
from collections import deque

n, m, v = list(map(int, sys.stdin.readline().strip().split()))

# graph 간선 정보 읽어오기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))
    graph[p1].append(p2)
    graph[p2].append(p1)

# 올바른 bfs 순서를 위해 정렬하기
for i in range(len(graph)):
    graph[i] = sorted(graph[i])

visited = [False]*(n+1) # 정점의 번호가 0이 아닌 1부터 시작하므로 n+1 을 곱해준다.
# dfs 함수 정의
def dfs(idx):
    print(idx, end=" ") # 탐색을 하면서, 노드 하나 진행할 때마다 출력한다.
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)
            visited[i] = True # 원래 전체 graph를 dfs할 때는 False 여야 하는 부분! (지금은 더 갈 노드가 없을 때까지만 가기 때문에 True)

def bfs(idx):
    q = deque([idx])
    visited[idx] = True
    while q:
        now = q.popleft()
        print(now, end=" ") # 탐색을 하면서, 노드 하나 진행할 때마다 출력한다.
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False]*(n+1)
bfs(v)


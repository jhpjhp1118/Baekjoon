# https://www.acmicpc.net/problem/11725
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))

    graph[p1].append(p2)
    graph[p2].append(p1)

parent = [-1]*(n + 1) # 부모 노드를 기록하는 리스트. 인덱스를 맞추느라 0, 1 번째 값은 의미없다.
visited = [False]*(n + 1) # 방문했는지 기록하는 리스트
visited[1] = True # 1번 노드는 방문했다고 간주한다.

q = deque()
# 1번 노드의 자식 노드들의 부모 --> 1번 노드라고 기록한다.
for i in graph[1]:
    parent[i] = 1
    visited[i] = True
    q.append(i)

while q:
    now = q.popleft()

    # 탐색된 자식(now)이 또다른 노드의 부모가 되는지 확인한다.
    for i in graph[now]:
        # 만약 방문하지 않은 노드일 경우
        if not visited[i]:
            # now 노드가 탐색된 노드의 부모가 된다.
            parent[i] = now
            visited[i] = True
            q.append(i)

# 2번 노드부터 마지막 노드까지 부모 노드를 출력한다.
for i in range(2, n + 1):
    print(parent[i])





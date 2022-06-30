# https://www.acmicpc.net/problem/1707
import sys 
from collections import deque

t = int(sys.stdin.readline().strip())

"""
아이디어: bfs로 안 가본 곳들만 탐색하면서, 현재 탐색의 중심 노드와 번호가 같은 것이 나오면, 
바로 탐색을 종료하고 No 를 출력한다.
만약 탐색이 다 끝날 때까지 번호가 같은 것이 나오지 않는다면, Yes를 출력한다.

정의: 노드들을 2개의 집합으로 나눈다. (0을 붙인 노드) vs (1을 붙인 노드)
아예 한번도 방문하지 않은 노드는 -1로 처음부터 정의한다

주의) 간선이 없는 노드가 있을 수 있다! 
"""

def bfs(visited, start):
    # 만약 인접한 노드끼리 같은 번호인 경우가 나오면, 바로 False가 리턴된다.
    if visited[start] != -1:
        return True
    visited[start] = 0
    q= deque([start])

    while q:
        now = q.popleft()
        for i in graph[now]:
            # 처음 가보는 노드인 경우
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] ^ 1
            # 이미 가본 노드이고, 같은 번호의 노드여서 문제가 있는 경우           
            elif visited[i] == visited[now]:
                return False
            # 이미 가본 노드이고, 다른 번호의 노드여서 문제가 없는 경우
            else: 
                continue
    
    return True

for _ in range(t):

    n, m = list(map(int, sys.stdin.readline().strip().split()))

    # 간선 정보 읽어오기
    graph = [[] for i in range(n + 1)]
    visited = [-1]*(n + 1)
    visited[0] = 1000 # -1, 0, 1 이 아닌 의미없는 수로 만들어버리기

    for i in range(m):
        p1, p2 = list(map(int, sys.stdin.readline().strip().split()))
        graph[p1].append(p2)
        graph[p2].append(p1)

    

    # bfs 실행하기
    isYes = True
    for i in range(1, n + 1):
        flag = bfs(visited, start=i)
        if flag == False:
            isYes = False
            break
    
    if isYes == True:
        print("YES")
    else:
        print("NO")
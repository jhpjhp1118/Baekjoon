# https://www.acmicpc.net/problem/16947
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))
    graph[p1].append(p2)
    graph[p2].append(p1)


global isCycle, cycleNodes, minDists
isCycle = False
cycleNodes = []

# 순환선이 어떤 노드들로 이루어져 있는지 찾는 함수
def find_cycle(idx, start, graph, visited, cycle):
    global isCycle, cycleNodes
    if isCycle:
        return

    for i in graph[idx]:
        if i == start and len(cycle) >= 3:
            cycleNodes = cycle
            isCycle = True
            return

        if not visited[i]:
            visited[i] = True
            find_cycle(i, start, graph, visited, cycle + [i])
            visited[i] = False

# 순환선으로부터 최소거리를 dfs 방식으로 찾는 함수
def count_distance(idx, cnt, visited, cycleMask):
    global minDists
    minDists[idx] = cnt

    for i in graph[idx]:
        if not visited[i] and not cycleMask[i]:
            visited[i] = True
            
            count_distance(i, cnt + 1, visited, cycleMask)
            visited[i] = False


# 먼저 순환선을 이루는 노드들이 무엇인지 찾는다
visited = [False]*(n + 1)

for i in range(1, n + 1):
    visited[i] = True
    find_cycle(i, i, graph, visited, cycle=[i])
    
    if isCycle:
        break


# 순환선 노드 중, 순환선이 아닌 노드와 연결된 것들을 찾아서, dfs로 최소 거리 찾으면서 기록해나가기
minDists = [0]*(n + 1)

cycleMask = [False] * (n + 1)
for i in cycleNodes:
    cycleMask[i] = True

visited = [False]*(n + 1)
for i in cycleNodes:
    for j in graph[i]:
        if not cycleMask[j]:
            visited[j] = True
            count_distance(j, 1, visited, cycleMask)



# 마지막에 노드 번호별로 최소 거리 출력하기
print(*minDists[1:])



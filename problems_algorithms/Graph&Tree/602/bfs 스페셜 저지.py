# https://www.acmicpc.net/problem/16940
import sys
from collections import deque
import copy

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))

    graph[p1].append(p2)
    graph[p2].append(p1)

seq = list(map(int, sys.stdin.readline().strip().split()))


# bfs를 실제로 돌려본다.
# 이 때, 한 층을 돌 때마다, 그 층의 개수만큼의 seq 부분 집합에, 해당 성분들이 빠짐없이 
# 모두 있는지 확인한다.


start = 1
q = deque([start])
qNext = deque()
idx = 0

visited = [False] * (n + 1)
visited[start] = True

if start != seq[0]:
    print(0)
    exit()
idx += 1

while True:
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                qNext.append(i)
                visited[i] = True

    if len(qNext) == 0:
        break

    seqCompare = set(seq[idx:idx + len(qNext)])

    if set(qNext) != seqCompare:
        print(0)
        exit()

    # check = all(i in qNext for i in seqCompare)

    # if not check:
        # print(0)
        # exit()    
    # for i in qNext:
    #     if i not in seqCompare:
    #         print(0)
    #         exit()
    #     seqCompare.remove(i)


    idx += len(qNext)
    while qNext:
        q.append(qNext.pop())
    qNext = deque()


print(1)




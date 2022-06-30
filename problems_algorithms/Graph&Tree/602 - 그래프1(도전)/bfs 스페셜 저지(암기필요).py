# https://www.acmicpc.net/problem/16940
import sys
from collections import deque

# 참고링크: https://vixxcode.tistory.com/28

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
# 주의) 가지노드마다 순서가 존재한다. 그 순서도 지켜지는지 확인하자! 
# 즉, 같은 층의 노드들도, 어느 노드의 가지노드들인지는 순서를 지켜야 한다!


start = 1
q = deque([start])
stk = deque()
idx = 0

visited = [False] * (n + 1)
visited[start] = True

# 시작노드가 일치하는지(1이 맞는지) 확인
if start != seq[0]:
    print(0)
    exit()
idx += 1


while q:
    stk = deque() # 한 노드의 가지노드들만 저장하기 위한 스택
    now = q.popleft()
    
    # bfs 방식으로, 한 노드에 대해 한 단계 탐색하기
    for i in graph[now]:
        if not visited[i]:
            stk.append(i)
            visited[i] = True

    # bfs 방문 순서와 stk가 동일한 성분들을 가지는지 확인한다.
    seqCompare = seq[idx:idx + len(stk)]
    if set(stk) != set(seqCompare):
        print(0)
        exit()
    # 다음의 확인을 위해, bfs 방문 순서의 인덱스를 옮겨준다.
    idx += len(stk)

    # 해당 노드의 가지 노드들(다음 탐색 후보들)을 q에 추가시킨다.
    for i in seqCompare:
        q.append(i)

print(1)

# 참고! q에는 꼭 한 단계의 노드들만 있는 것이 아니다! 인접한 두 단계의 노드들이 섞여 있을 수 있다!
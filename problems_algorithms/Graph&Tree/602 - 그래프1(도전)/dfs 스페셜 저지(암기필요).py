# https://www.acmicpc.net/problem/16964
import sys

# 참고링크: https://vixxcode.tistory.com/29
# 의문점?: 예시문제에 대해, 1 4 2 3 이면 틀린 답인데도 1이 출력된다. 이래도 괜찮은가?
            # --> 추측: 노드 순서를 아예 틀려버리는 답은 제시하지 않는 것 같다.
n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))

    graph[p1].append(p2)
    graph[p2].append(p1)

seq = list(map(int, sys.stdin.readline().strip().split()))

level = [0]*(n + 1) # 각 노드의 깊이 기록
tsize = [0]*(n + 1) # 각 노드를 기준으로, 끝까지 내려갔을 때 나오는 총 노드의 갯수들 기록
visited = [False]*(n + 1) # 방문 여부 기록

def dfs(idx, lv):
    if visited[idx]:
        return 0

    visited[idx] = True
    # size 초기화
    size = 1
    # 깊이 기록하기
    level[idx] = lv

    for i in graph[idx]:
        # dfs를 수행하면서, tree size 측정하기
        size += dfs(i, lv + 1)

    # 해당 가지의 끝까지 찍고 온 뒤, 가지의 크기를 기록한다
    tsize[idx] = size
    return size

if seq[0] != 1:
    print(0)
    exit()
else:
    dfs(1, 0)
    for i in range(1, n):
        x = seq[i]
        # 자식이 더 없는 노드이거나, ans 순서 상으로 마지막 가지이면 skip 한다?
        if tsize[x] == 1 or i + tsize[x] >= n:
            continue
        
        # i번째로 제시된 노드가 속한 가지 --> 다음 가지에 속했을걸로 예상되는, 같은 깊이의 노드
        # 즉, 같은 깊이의 다음 가지로 넘어간다.
        next = seq[i + tsize[x]]

        # 현재 seq 노드보다, 같은 깊이 & 다음 가지로 추정되는 노드의 깊이가, 더 깊은 경우 틀린 순서이다.
        # 즉, 같은 깊이가 나오길 기대했는데 틀린 경우를 찾는 것이다.
        if level[x] < level[next]:
            print(0)
            exit()

    print(1)




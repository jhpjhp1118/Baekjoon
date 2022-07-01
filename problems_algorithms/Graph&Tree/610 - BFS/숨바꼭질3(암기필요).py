# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
import copy

n, k = list(map(int, sys.stdin.readline().strip().split()))

visited = [-1]*100001 # 아직 방문하지 않았으면 -1, 방문했으면 최소 거리 기록하기

# 취할 수 있는 3가지 행동 +1, -1, *2
def action(num, opt):
    if opt == 1:
        return num + 1
    elif opt == 2:
        return num - 1
    else:
        return num*2

q = deque([n])
qNext = deque()
visited[n] = 0 # 처음 위치엔 0 값 넣기

# 처음부터 같은 위치에 있을 경우
if n == k:
    print(0)
    exit()

# 해당 q를 탐색하다가, 목표지인 k를 발견하면 True가 된다.
flag = False # flag가 True이면, 이번 q가 다 소진될 때까지만 탐색하고 종료한다.
while True:
    while q:
        now = q.popleft()
        
        # 3가지 행동을 전부 탐색한다.
        for opt in range(1, 4):
            val = action(now, opt)

            # 목표지인 동생의 위치일 경우, flag를 True로 바꿔준다.
            if val == k:
                flag = True

            # 범위 밖으로 나갈 경우, skip한다.
            if val < 0 or val > 100000:
                continue

            # 이미 방문한 곳일 때
            if visited[val] != -1:
                # 2배해주는 action에는, now의 최소이동횟수를 그대로 비교해준다.
                if opt == 3:
                    compare = visited[now]
                # 그 외의 action에는, + 1 한 최소 이동횟수를 비교해준다.
                else:
                    compare = visited[now] + 1
                
                # 기존의 최소이동횟수 or 비교값 중 더 작은 것으로 갱신한다.
                if visited[val] <= compare:
                    continue
                else:
                    visited[val] = compare
            
            qNext.append(val)

            # 처음 방문하는 곳일 때
            # 2배해주는 action에는, now의 최소이동횟수를 그대로 기록해준다.
            if opt == 3:
                visited[val] = visited[now]
            # 그 외의 action에는, + 1 한 최소 이동횟수를 기록해준다.
            else:
                visited[val] = visited[now] + 1
    if flag:
        print(visited[k])
        exit()
    q = copy.deepcopy(qNext)

    qNext = deque()


# 반례: 4 6 --> 1 (4 - 3 - 6)
#  -->!!! 목표값을 만나면 바로 exit을 해버려서 그렇다. 
# q가 끝날때까지만 기다려보자

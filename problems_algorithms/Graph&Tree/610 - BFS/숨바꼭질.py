# https://www.acmicpc.net/problem/1697
import sys
from collections import deque
import copy

n, k = list(map(int, sys.stdin.readline().strip().split()))

visited = [-1]*200001 # 아직 방문하지 않았으면 -1, 방문했으면 최소 거리 기록하기

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
    print(visited[k])
    exit()

while True:
    while q:
        now = q.popleft()
        
        # 3가지 행동을 전부 탐색한다.
        for opt in range(1, 4):
            val = action(now, opt)
            # 동생의 위치일 경우, 직전 최소 이동 횟수 + 1 을 출력하고, 프로그램을 종료한다.
            if val == k:
                print(visited[now] + 1)
                exit()
            # 범위 밖으로 나갈 경우, skip한다.
            if val < 0 or val > 100000:
                continue
            # 이미 방문한 곳이면, skip한다.
            if visited[val] != -1:
                continue
            
            qNext.append(val)
            visited[val] = visited[now] + 1

    q = copy.deepcopy(qNext)

    qNext = deque()

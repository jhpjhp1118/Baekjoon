# https://www.acmicpc.net/problem/13913
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

# 역으로 취할 수 있는 3가지 행동 -1, +1, //2
def actionInverse(num, opt):
    if opt == 1:
        return num - 1
    elif opt == 2:
        return num + 1
    else:
        return num//2

def findPath(n, k, visited, minDist):
    
    path = deque([k]) # 경로
    dist = minDist # pos ~ n까지 남은 이동 횟수
    pos = k # 현재 위치

    while dist > 0:
        for opt in range(1, 4):
            # opt가 3인데, 숫자가 2로 나누어떨어지지 않을경우, skip한다.
            if opt == 3 and pos % 2 != 0:
                continue
            
            now = actionInverse(pos, opt)
            # 만약 방문한 곳 위치에서 1칸만 움직여서 pos로 갈 수 있다면, 그 방문한 곳으로 간다.
            if visited[now] == dist - 1:
                dist = visited[now] # 남은 거리 갱신해주기
                path.appendleft(now) # 경로 저장
                pos = now # 현재 위치 갱신
                break
    return list(path) # path를 list화하여 반환한다.


q = deque([n])
qNext = deque()
visited[n] = 0 # 처음 위치엔 0 값 넣기

# 처음부터 같은 위치에 있을 경우
if n == k:
    print(visited[k])
    print(n)
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
                path = findPath(n, k, visited, visited[now] + 1)
                print(*path)
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

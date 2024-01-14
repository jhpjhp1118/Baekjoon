# https://www.acmicpc.net/problem/3190

import sys
from collections import deque

N = int(sys.stdin.readline().strip()) # 그리드의 크기 (N x N)
K = int(sys.stdin.readline().strip()) # 사과의 개수

# 그리드 초기화
grid = [[0]*N for _ in range(N)]

# 사과 위치 읽기
for _ in range(K):
    r, c = list(map(int, sys.stdin.readline().strip().split()))
    grid[r-1][c-1] = 'apple' # !! 사과를 어떤 형태로 저장할지는 변할 수 있음!

L = int(sys.stdin.readline().strip()) # 방향 전환 횟수
# 방향 전환 읽기
moveInfo = deque()
for _ in range(L):
    length, direction = sys.stdin.readline().strip().split()
    length = int(length)
    moveInfo.append([length, direction])

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
idxDir = 100 # L이 최대 100이므로 100으로 초기화
dirCurr = [0, 1] # 오른쪽으로 초기화
moveInfoCurr = moveInfo.popleft()
# 뱀 초기화
head = (0, 0)
snake = deque()
snake.append(head)
# 시간 초기화
time = 0
while True:
    # 방향 전환해야하는지 확인하고, 방향 전환 하던지 말던지
    if time == moveInfoCurr[0]:
        if moveInfoCurr[1] == 'D':
            idxDir += 1
        elif moveInfoCurr[1] == 'L':
            idxDir += -1

        dirCurr = directions[idxDir%4]

        if len(moveInfo) > 0:
            moveInfoCurr = moveInfo.popleft()

    # 머리의 다음 행선지 head 를 구한다
    head = (head[0] + dirCurr[0], head[1] + dirCurr[1])
    # 시간 increment
    time += 1
    # head 가 벽을 벗어나면 멈춘다
    if head[0] < 0 or head[0] > N - 1 or head[1] < 0 or head[1] > N - 1:
        break
    # head 가 이미 snake에 있으면 멈춘다
    if head in set(snake):
        break

    # snake에 head를 appendleft 해준다
    snake.appendleft(head)
    # headNext 에 사과가 있으면,
    if grid[head[0]][head[1]] == 'apple':
        grid[head[0]][head[1]] = 0
    else:
        snake.pop()


# 시간 출력
print(time)



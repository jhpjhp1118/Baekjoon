# https://www.acmicpc.net/problem/12100
import sys
from collections import deque
import copy

input = sys.stdin.readline

n = int(input().strip())

grid = [list(map(int, input().strip().split())) for _ in range(n)]

# 움직일 수 있는 방향에 대한 리스트
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # format: (세로, 가로)

ans = 0


# 움직임을 시행하는 함수
# dir 방향의 끝에 있는 성분부터 역순으로 차례로, 만약 pair가 있으면, 2개씩만 pair를 지어서 합쳐준다.
def move(grid, dir):
    global ans

    gridNext = [[0]*n for _ in range(n)] # 다음 단계의 grid가 될 것

    # dir가 가로인지 세로인지에 따라, row / col의 non-zero 성분들을 확인한다.
    # 가로일 경우
    if dir[0] == 0:
        for i in range(n):
            # non-zero 성분들 확인하기
            nonzeros = deque([grid[i][j] for j in range(n) if grid[i][j] != 0])
            
            # 끝에서부터 차례대로, 
            arranged = deque()

            # 오른쪽으로 움직이는 경우
            if dir[1] == 1:
                # nonzeros의 성분이 남아있을 때까지만 loop를 돈다.
                while nonzeros:
                    val = nonzeros.pop()
                    # nonzeros의 오른쪽 끝 성분 == 오른쪽 2번째 성분일 경우, 합쳐준다.
                    if len(nonzeros) >= 1 and val == nonzeros[-1]:
                        nonzeros.pop()
                        arranged.appendleft(2 * val)
                    # 전혀 다른 값일 경우, 그대로 보존한다.
                    else:
                        arranged.appendleft(val)

                # arranged에 성분이 존재할 경우, 최대값을 갱신한다.
                if arranged:
                    ans = max(ans, max(arranged))

                # 해당 row의 오른쪽 끝에서부터 값을 채워준다.
                for j in range(len(arranged)):
                    gridNext[i][n - j - 1] = arranged.pop()

            # 왼쪽으로 움직이는 경우
            else:
                # nonzeros의 성분이 남아있을 때까지만 loop를 돈다.
                while nonzeros:
                    val = nonzeros.popleft()
                    # nonzeros의 오른쪽 끝 성분 == 오른쪽 2번째 성분일 경우, 합쳐준다.
                    if len(nonzeros) >= 1 and val == nonzeros[0]:
                        nonzeros.popleft()
                        arranged.append(2 * val)
                    # 전혀 다른 값일 경우, 그대로 보존한다.
                    else:
                        arranged.append(val)

                # arranged에 성분이 존재할 경우, 최대값을 갱신한다.
                if arranged:
                    ans = max(ans, max(arranged))

                # 해당 row의 왼쪽 끝에서부터 값을 채워준다.
                for j in range(len(arranged)):
                    gridNext[i][j] = arranged.popleft()

                
    # 세로일 경우
    else:
        for i in range(n):
            # non-zero 성분들 확인하기
            nonzeros = deque([grid[j][i] for j in range(n) if grid[j][i] != 0])
            # print("nonzeros:", nonzeros, i) # !!!
            
            # 끝에서부터 차례대로, 
            arranged = deque()

            # 아래쪽으로 움직이는 경우
            if dir[0] == 1:
                # nonzeros의 성분이 남아있을 때까지만 loop를 돈다.
                while nonzeros:
                    val = nonzeros.pop()
                    # nonzeros의 아래쪽 끝 성분 == 아래쪽 2번째 성분일 경우, 합쳐준다.
                    if len(nonzeros) >= 1 and val == nonzeros[-1]:
                        nonzeros.pop()
                        arranged.appendleft(2 * val)
                    # 전혀 다른 값일 경우, 그대로 보존한다.
                    else:
                        arranged.appendleft(val)

                # arranged에 성분이 존재할 경우, 최대값을 갱신한다.
                if arranged:
                    ans = max(ans, max(arranged))

                # 해당 row의 아래쪽 끝에서부터 값을 채워준다.
                for j in range(len(arranged)):
                    gridNext[n - j - 1][i] = arranged.pop()

            # 위쪽으로 움직이는 경우
            else:
                # nonzeros의 성분이 남아있을 때까지만 loop를 돈다.
                while nonzeros:
                    val = nonzeros.popleft()
                    # nonzeros의 위쪽 끝 성분 == 위쪽 2번째 성분일 경우, 합쳐준다.
                    if len(nonzeros) >= 1 and val == nonzeros[0]:
                        nonzeros.popleft()
                        arranged.append(2 * val)
                    # 전혀 다른 값일 경우, 그대로 보존한다.
                    else:
                        arranged.append(val)

                # arranged에 성분이 존재할 경우, 최대값을 갱신한다.
                if arranged:
                    ans = max(ans, max(arranged))

                # 해당 row의 위쪽 끝에서부터 값을 채워준다.
                for j in range(len(arranged)):
                    gridNext[j][i] = arranged.popleft()

    return gridNext


q = deque()
q.append(grid)
qNext = deque()

cnt = 0
# 이동횟수가 5일 때까지만 탐색한다.
while cnt < 5:
    while q:
        g = q.popleft()
        for dir in dirs:
            gNext = move(g, dir)
            qNext.append(gNext)

    q = copy.deepcopy(qNext)
    qNext = deque()
    cnt += 1

print(ans)




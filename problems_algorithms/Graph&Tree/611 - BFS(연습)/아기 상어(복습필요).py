# https://www.acmicpc.net/problem/16236
import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())

grid = []
baby = (-1, -1, 2, 0) # 아기 상어의 row좌표, col좌표, 크기, 크기가 바뀌고 나서 먹은 누적 물고기 갯수
for i in range(n):
    line = list(map(int, input().strip().split()))
    for j in range(n):
        # 아기 상어 위치 기록하기
        if line[j] == 9:
            baby = (i, j, 2, 0)
            line[j] = 0 # 아기 상어 위치는 미리 빈 칸으로 만들어 놓기
    grid.append(line)
    
# 가장 위 & 가장 왼쪽에 위치한 물고기를 먹어야하므로, 상 --> 좌 --> 우 --> 하 순으로 배치했다. !!!
steps = [(-1, 0), (0, -1), (0, 1), (1, 0)]


# 물고기 먹기에 대한 함수
def eat_fish(grid, baby, n, steps):
    # 방문 여부 & 해당 칸에 도달하기 위해 필요한 이동 횟수 기록하기 위한 grid 생성
    visited = [[-1]*n for _ in range(n)]
    visited[baby[0]][baby[1]] = 0 # 현재 아기 상어 위치에 대해 초기화
    babySize = baby[2]
    numEaten = baby[3]

    q = deque()
    q.append((baby[0], baby[1]))

    # 먹을 수 있는 물고기가 나타났을 때, 비교 mode로 바꾸기 위한 bool 변수
    isCompare = False
    pos = (30, 30) # 최대 n 값이 20이므로, 적당히 큰 좌표값으로 초기화

    while q:
        for _ in range(len(q)):
            nr, nc = q.popleft()

            # 해당 위치에 먹을 수 있는 물고기가 있을 경우, 최적의 물고기 위치를 비교해서 찾는다.
            if grid[nr][nc] != 0 and grid[nr][nc] < babySize:
                isCompare = True

                # 더 위쪽에 있는 후보 물고기 위치가 나온 경우, pos를 그것으로 바꿔준다.
                if nr < pos[0]:
                    pos = (nr, nc)
                # 같은 높이에 있지만, 더 왼쪽에 있는 후보 물고기 위치가 나온 경우, pos를 그것으로 바꿔준다.
                elif nr == pos[0] and nc < pos[1]:
                    pos = (nr, nc)


            # 먹을 수 있는 물고기가 하나라도 발견된 상태면, 최적 위치의 물고기 찾기에만 집중하기 위해, 다음 칸으로의 전진을 skip 한다.
            if isCompare:
                continue

            for step in steps:
                r, c = nr + step[0], nc + step[1]

                # 후보칸이 grid 범위를 벗어나거나, 이미 방문했을 경우, skip 한다.
                if r < 0 or r >= n or c < 0 or c >= n or visited[r][c] != -1:
                    continue

                # 후보칸에 물고기가 있을 경우,
                if grid[r][c] != 0:
                    # 아기 상어 크기 이하의 물고기일 경우, q에 추가한다. (즉, 먹을 수 있거나 / 그냥 지나가기만 하거나)
                    if grid[r][c] <= babySize:
                        visited[r][c] = visited[nr][nc] + 1
                        q.append((r, c))
                # 빈 칸일 경우,
                else:
                    visited[r][c] = visited[nr][nc] + 1
                    q.append((r, c))

        # 먹을 수 있는 최적 위치의 물고기가 발견된 경우,
        if isCompare:
            nr, nc = pos
            grid[nr][nc] = 0  # 해당 물고기 칸을 빈 칸으로 만든다.
            numEaten += 1 # 먹은 누적 물고기 갯수를 1만큼 증가시킨다.
            # 먹은 누적 물고기 갯수가, 현재 아기 상어 크기와 같아졌을 경우, 누적 물고기 갯수를 0으로 되돌리고, 아기 상어 크기를 1 증가시킨다.
            if numEaten == babySize:
                numEaten = 0
                babySize += 1

            return (nr, nc, babySize, numEaten), True, visited[nr][nc]

    # 먹을 수 있는 물고기가 없을 경우, False를 리턴한다.
    return baby, False, 0

ans = 0
# 먹을 수 있는 물고기가 남아있을 때까지 계속 반복한다.
while True:
    baby, isEat, cnt = eat_fish(grid, baby, n, steps)
    # 이번 action에서 물고기를 먹지 않았으면, 탐색을 종료한다.
    if not isEat:
        break
    # 이동 횟수를 더해준다.
    ans += cnt

print(ans)

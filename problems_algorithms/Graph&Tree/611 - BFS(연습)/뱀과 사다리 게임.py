# https://www.acmicpc.net/problem/16928
import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

# 1에서 시작해서 100으로 향해 간다. 0번 칸은 무시한다. (index 맞추기용)
grid = [0] * 101
visited = [0] * 101 # 방문 여부 확인용. 이미 방문한 곳은, 그 당시 횟수가 최소 횟수였을 것이므로, 다시 방문할 필요 없다.

# 사다리나 뱀이 연결된 칸은, 목표지 칸을 쓴다.
for _ in range(n):
    x, y = list(map(int, input().strip().split()))
    grid[x] = y

for _ in range(m):
    u, v = list(map(int, input().strip().split()))
    grid[u] = v

# 초기화
q = deque()
q.append(1) # 처음 시작하는 칸을 append한다.
qNext = deque()

cnt = 1

while True:
    while q:
        now = q.popleft()
        # 주사위 1 ~ 6 까지 탐색한다.
        for dice in range(1, 7):
            # 다음 칸 후보
            next = now + dice
            # 다음 칸 후보가 100을 넘어버리거나, 이미 방문한 적이 있는 경우, skip 한다.
            if next > 100 or visited[next] != 0:
                continue
            # 목표지인 100이 나올 경우, 이동 횟수를 출력하고 종료한다.
            if next == 100:
                print(cnt)
                exit()
            # 방문한 칸을 표기한다.
            visited[next] = 1
            # 사다리나 뱀이 있을 경우,
            if grid[next] != 0:
                # 사다리나 뱀의 목표칸에도 방문 여부를 표기한다.
                visited[grid[next]] = 1
                # 사다리나 뱀의 목표칸을 다음 탐색 후보로 추가한다.
                qNext.append(grid[next])

            else:
                # 다음 칸 후보를 다음 탐색 후보로 추가한다.
                qNext.append(next)

    cnt += 1

    q = copy.deepcopy(qNext)
    qNext = deque()

# https://www.acmicpc.net/problem/16948
import sys
from collections import deque
import copy

"""
주의) 도달하지 못하는 칸의 규칙을 찾는다기보단, 가능한 모든 칸을 전부 다 가보고, 못간 칸일 경우 -1을 출력한다.
"""

input = sys.stdin.readline
n = int(input())
# 최소 이동 횟수를 기록하는 grid
visited = [[-1]*n for _ in range(n)]


r1, c1, r2, c2 = list(map(int, input().strip().split()))
visited[r1][c1] = 0 # 출발지는 이동 횟수가 0이다.

# 이동 가능한 방법들을 담아놓은 리스트
steps = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

q = deque()
q.append((r1, c1))
qNext = deque()

cnt = 1
while True:
    while q:
        now = q.popleft()

        for step in steps:
            rTarget, cTarget = now[0] + step[0], now[1] + step[1]
            # 종료칸을 찾아내면, 이동 횟수를 출력하고 종료한다.
            if rTarget == r2 and cTarget == c2:
                print(cnt)
                exit()
            # grid 범위를 벗어나거나, 이미 방문한 칸이면, skip 한다.
            if rTarget >= n or rTarget < 0 or cTarget >= n or cTarget < 0 or visited[rTarget][cTarget] != -1:
                continue

            qNext.append((rTarget, cTarget))
            visited[rTarget][cTarget] = cnt

    # 만약 다음 탐색 대상이 더 이상 없을 경우, 탐색을 종료한다. (결국 -1 출력하기용)
    if not qNext:
        break

    cnt += 1
    q = copy.deepcopy(qNext)
    qNext = deque()

# 도달하지 못하는 칸일 경우, -1을 출력한다.
print(visited[r2][c2])


# https://www.acmicpc.net/problem/16933
import sys
from collections import deque

input = sys.stdin.readline

"""
아이디어: 벽 파괴 기회를 사용한 횟수에 따라, 방문 여부 & 최소 이동 횟수를 기록하는 grid를 사용한다.
        day라는 이동 횟수를 의미하는 전역 변수를 두고, 이것을 점차 증가시켜가며 최소 이동 횟수를 기록해간다.
"""

n, m, k = list(map(int, input().strip().split()))

maze = []
for i in range(n):
    line = list(map(int, list(input().strip())))
    maze.append(line)

# 벽 파괴 여부에 따라 최소 이동 횟수를 기록하는 grid 생성
# 3차원: 0 --> 벽을 1번도 파괴하지 않고 갈 때의 이동 횟수
#       x(=1, 2, 3, ...k - 1) --> 벽을 x번 파괴한 상태로 갈 때의 이동 횟수
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

q = deque()
q.append((0, 0, 0)) # 형식: row / col / 벽 파괴 여부(boom!)

steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
day = 1 # 양수 --> 낮 / 음수 --> 밤
while q:
    # 지금 낮인지 밤인지 확인한다.
    isNight = False if day > 0 else True
    # 한 이동 횟수에 대한 경우만 탐색한다.
    for _ in range(len(q)):
        nr, nc, boom = q.popleft()
        today = abs(day) # 이동 횟수의 절대값을 확인한다.

        # 도착지 칸에 도착하면, 최소 이동횟수를 출력하고 종료한다.
        if nr == n - 1 and nc == m - 1:
            print(visited[nr][nc][boom])
            exit()

        for step in steps:
            r, c = nr + step[0], nc + step[1]
            # grid 범위를 벗어날 경우, skip 한다.
            if r < 0 or r >= n or c < 0 or c >= m or visited[r][c][boom] != 0:
                continue

            # 타겟으로 하는 칸이 빈 칸이면, 단순하게 이동한다.
            if maze[r][c] == 0:
                visited[r][c][boom] = today + 1
                q.append((r, c, boom))

            # 타겟으로 하는 칸이 벽이고, 아직 벽 파괴 기회가 남아있고,
            # 아직 한번도 방문하지 않은 곳이면,
            if maze[r][c] == 1 and boom < k and visited[r][c][boom + 1] == 0:
                # 낮일 경우, 벽을 파괴하고 전진한다.
                if not isNight:
                    visited[r][c][boom + 1] = today + 1
                    q.append((r, c, boom + 1))
                # 밤일 경우, 제자리에서 하루 기다려 본다.
                else:
                    q.append((nr, nc, boom))

    # 이동 횟수를 1만큼 더해주고, 낮/밤을 바꾼다.
    day = day + 1 if day > 0 else day - 1
    day *= -1


# 해결을 못하는 미로일 경우, -1을 출력하고 종료한다.
print(-1)



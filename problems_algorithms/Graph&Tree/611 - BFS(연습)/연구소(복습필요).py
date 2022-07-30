# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
import copy

"""
아이디어:
- 모든 0 중 3개를 선택해서, 1로 바꾼다.
    - 중복되지 않게 선택해야 함 --> 어떻게???
- 모든 2를 seed로 해서 바이러스를 퍼트린다
- 남은 0의 갯수를 센다.
    - 바이러스를 퍼트릴 때, cnt 변수를 둬서 효율적으로 셀 수 있다.
- 최대값을 갱신한다.
"""

input = sys.stdin.readline
n, m = list(map(int, input().strip().split()))

grid = []
empty = []
virus = []
for i in range(n):
    line = list(map(int, input().strip().split()))
    grid.append(line)
    # 빈칸 & virus seed를 미리 찾아놓는다.
    for j in range(m):
        if line[j] == 0:
            empty.append((i, j))

        elif line[j] == 2:
            virus.append((i, j))

def spreadVirus(gridTest, virus, cntMin):
    # 상, 하, 좌, 우 리스트
    steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    q = deque()
    # 바이러스 seed들을 q에 추가한다.
    for v in virus:
        q.append(v)

    # 전염되어버린 빈칸 세는 변수 (*효율*)
    cntSpread = 0
    while q:
        now = q.popleft()
        for step in steps:
            r, c = now[0] + step[0], now[1] + step[1]
            # grid 범위를 넘거나, 벽에 가로막히거나, 이미 바이러스가 퍼진 곳이면, skip한다.
            if r < 0 or r >= n or c < 0 or c >= m or gridTest[r][c] != 0:
                continue

            gridTest[r][c] = 2
            q.append((r, c))
            cntSpread += 1
            # 만약 지금까지의 최소값보다 더 많이 퍼트려질 경우, 거기서 탐색을 종료한다. (*효율*)
            if cntSpread >= cntMin:
                return 10000

    return cntSpread


numEmpty = len(empty)
ans = 0
cntMin = 10000
# 3개의 벽을 세우는 모든 경우에 대해 탐색한다. <-- dfs로도 구현 가능!!
for i in range(0, numEmpty - 2):
    for j in range(i, numEmpty - 1):
        for k in range(j, numEmpty):
            # grid 복사해오기
            gridTest = copy.deepcopy(grid)
            # 벽 3개 가져오기
            wall1, wall2, wall3 = empty[i], empty[j], empty[k]
            # 벽 세우기
            gridTest[wall1[0]][wall1[1]] = 1
            gridTest[wall2[0]][wall2[1]] = 1
            gridTest[wall3[0]][wall3[1]] = 1
            # 해당 grid 상태에서의 virus가 퍼진 (원래 빈칸이었던) 칸의 갯수 세기
            cntSpread = spreadVirus(gridTest, virus, cntMin)
            # 최소값 갱신하기
            cntMin = min(cntMin, cntSpread)
# 답: 기존 빈 칸 - 새로 세운 3개의 벽 - 최소 퍼진 칸의 갯수
print(numEmpty - 3 - cntMin)









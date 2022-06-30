# https://www.acmicpc.net/problem/2667
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

data = []
for _ in range(n):
    data.append(list(map(int, list(sys.stdin.readline().strip()))))

"""
좌표 방식 정의 ex)
0 1 2
3 4 5
6 7 8

"""
# 방문한 곳 기록하기
visited = [False]*(n**2)

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# 집합들 구분해서 묶어내가기
sets = []

q = deque([])
for i in range(n**2):
    row, col = i//n, i%n # row, col 위치 계산하기

    setnow = []

    # 해당 위치의 값이 1일 때만 걸러내기
    if data[row][col] == 0:
        visited[i] = True
        continue

    # 상하좌우 탐색하기
    # 탐색 규칙: 1칸 이동했을 때, data = 1 이면, 그곳을 중심으로 계속 탐색해간다. (bfs 방식으로)
    # 이 때, que에 칸을 저장할 때, 좌표 번호 1개짜리로 기록한다.

    # 왼쪽 위 --> 오른쪽 아래로 한칸씩 보면서, 해당 좌표의 값이 1이고, 한번도 안가본 칸이면, 집합 탐색을 시작한다.
    if not visited[i]:
        q.append(i)
        visited[i] = True
        setnow.append(i)

    while q:
        now = q.popleft()
        # 탐색의 중심 칸을 좌표로 변환한다.
        row, col = now // n, now % n
        for step in steps:
            # 상하좌우 칸을 하나씩 좌표로 변환하면서 탐색한다.
            r, c = row + step[0], col + step[1]
            target = n * r + c
            # 칸의 위치가 grid의 칸 범위 안에 포함되고, 한번도 안가본 칸만 통과시킨다.
            if 0 <= r < n and 0 <= c < n and not visited[target]:
                visited[target] = True
                # 해당 칸의 값이 1이면, 현재 탐색중인 집합에 추가시킨다.
                if data[r][c] == 1:
                    setnow.append(target)
                    q.append(target)
    # 하나의 집합에 대한 탐색이 끝나고, 만약 현재 탐색중인 집합의 성분이 하나라도 있다면, sets에 추가한다.
    if setnow:
        sets.append(setnow)

# 집합들의 길이를 기준으로, 오름차순으로 정리하기
ans = []
for s in sets:
    ans.append(len(s))
ans = sorted(ans)

# 답 출력하기
print(len(ans))
for a in ans:
    print(a)


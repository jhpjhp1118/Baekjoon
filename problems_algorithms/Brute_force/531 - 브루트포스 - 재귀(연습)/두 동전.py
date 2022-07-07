# https://www.acmicpc.net/problem/16197
import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().strip().split()))

data = []

coins = []
for i in range(n):
    arr = list(sys.stdin.readline().strip())
    # 2개 동전의 위치를 모두 찾을 때까지는,
    if len(coins) != 2:
        # 각 row의 모든 성분을 하나씩 훑어보면서,
        for j in range(len(arr)):
            # 동전일 경우, 위치를 기록한다.
            if arr[j] == "o":
                coins.append((i, j))

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def move(r, c, step, data):
    rt, ct = r + step[0], c + step[1]

    if data[rt][ct] == "#":
        return r, c
    else:
        return rt, ct


q = deque()
q.append(coins)

ans = 0

while q:
    coinsNow = q.popleft()
    r1, c1 = coinsNow[0]
    r2, c2 = coinsNow[1]

    for step in steps:
        rt1, ct1 = move(r1, c1, step, data)
        rt2, ct2 = move(r1, c1, step, data)
        # rt1, ct1 = r1 + step[0], c1 + step[1]
        # rt2, ct2 = r2 + step[0], c2 + step[1]

        fallCount = 0

        # 각각의 동전이 빠졌는지 확인해서, 빠졌으면 fallCount를 + 1 한다
        if rt1 < 0 or rt1 > n - 1 or ct1 < 0 or ct1 > m - 1:
            fallCount += 1

        if rt2 < 0 or rt2 > n - 1 or ct2 < 0 or ct2 > m - 1:
            fallCount += 1

        # 동전이 하나만 빠지면 탐색을 완전 종료해버린다.
        if fallCount == 1:
            print(ans) # 답을 출력한다.
            exit()

        # 동전이 두개 다 빠지면, skip한다.
        elif fallCount == 2:
            continue

        # 동전이 하나도 안 빠지면, 다음 탐색 대상으로 추가한다.
        else:
            q.append([(rt1, ct1), (rt2, ct2)])



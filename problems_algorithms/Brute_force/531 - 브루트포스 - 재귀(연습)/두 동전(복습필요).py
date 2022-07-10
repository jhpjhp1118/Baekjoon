# https://www.acmicpc.net/problem/16197
import sys
from collections import deque
import copy

n, m = list(map(int, sys.stdin.readline().strip().split()))

data = []

coins = []
for i in range(n):
    arr = list(sys.stdin.readline().strip())
    data.append(arr)
    # 2개 동전의 위치를 모두 찾을 때까지는,
    if len(coins) != 4:
        # 각 row의 모든 성분을 하나씩 훑어보면서,
        for j in range(len(arr)):
            # 동전일 경우, 위치를 기록한다.
            if arr[j] == "o":
                coins.append(i)
                coins.append(j)

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def move(r, c, step, data):
    rt, ct = r + step[0], c + step[1]

    # 떨어지는 경우
    if rt < 0 or rt > n - 1 or ct < 0 or ct > m - 1:
        return -1, -1
    # 벽에 가로막히는 경우
    elif data[rt][ct] == "#":
        return r, c
    # 이동가능한 경우
    else:
        return rt, ct


q = deque()
q.append(coins)
qNext = deque()

ans = 0

while q:
    ans += 1
    while q:
        coinsNow = q.popleft()

        r1, c1 = coinsNow[0], coinsNow[1]
        r2, c2 = coinsNow[2], coinsNow[3]

        for step in steps:
            rt1, ct1 = move(r1, c1, step, data)
            rt2, ct2 = move(r2, c2, step, data)

            fallCount = 0

            # 각각의 동전이 빠졌는지 확인해서, 빠졌으면 fallCount를 + 1 한다
            if rt1 == -1 and ct1 == -1:
                fallCount += 1

            if rt2 == -1 and ct2 == -1:
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
                qNext.append((rt1, ct1, rt2, ct2))
    # 만약 10번을 넘게 움직여도 안되면, -1을 출력한다.
    if ans >= 10:
        print(-1)
        exit()

    # 가지치기: 완전히 중복되는 상태가 있으면, 하나로 줄여버린다. <-- 이것이 없으면 시간초과 발생!
    qNext = deque(set(qNext))

    q = copy.deepcopy(qNext)

    qNext = deque()


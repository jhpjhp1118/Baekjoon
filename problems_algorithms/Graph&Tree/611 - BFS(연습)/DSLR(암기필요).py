# https://www.acmicpc.net/problem/9019
import sys
from collections import deque

"""
주의) pypy3로 실행해야 시간초과 안뜸!
"""

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    a, b = list(map(int, input().strip().split()))

    # 방문여부를 표시하는 리스트 생성
    visited = [0]*10001
    visited[a] = 1

    q = deque()
    q.append((a, ""))

    while q:
        now, ans = q.popleft()
        # 목표하는 숫자가 나오면, 탐색을 종료한다.
        if now == b:
            print(ans)
            break

        # D
        target = now * 2 % 10000
        if visited[target] == 0:
            q.append((target, ans + "D"))
            visited[target] = 1

        # S
        if now == 0:
            target = 9999
        else:
            target = now - 1

        if visited[target] == 0:
            q.append((target, ans + "S"))
            visited[target] = 1

        # L
        target = (now * 10 + (now // 1000)) % 10000
        if visited[target] == 0:
            q.append((target, ans + "L"))
            visited[target] = 1

        # R
        target = ((now // 10) + 1000 * (now % 10)) % 10000
        if visited[target] == 0:
            q.append((target, ans + "R"))
            visited[target] = 1


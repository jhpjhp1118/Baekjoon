# https://www.acmicpc.net/problem/1783
import sys

input = sys.stdin.readline

"""
아이디어: 가로로 2칸 움직이는 선택지를 최소한으로 선택한다.
"""

n, m = list(map(int, input().strip().split()))

# 4가지 모든 움직임을 포함하여, 4번 이상의 이동을 수행할 수 있는 경우
if n >= 3 and m >= 7:
    # 가로로 2칸 움직이는 선택지는 2번만 포함하고, 나머지는 가로로 1칸 움직이는 선택지만 선택한 경우의 수
    ans = m - 2
# 4가지 모든 움직임을 포함할 수 없는 경우 (최대 4번이다)
else:
    # n = 2인 경우
    if n == 2:
        # 가로로 2칸 움직이는 선택지만 선택한 경우의 수 vs 4를 비교한다.
        ans = min(4, 1 + (m - 1) // 2)
    # n = 1인 경우
    elif n == 1:
        # 움직일 수 없다.
        ans = 1
    # n >= 3 인 경우,
    else:
        # 가로로 1칸 움직이는 선택지만 선택한 경우의 수 vs 4를 비교한다.
        ans = min(4, m)


print(ans)



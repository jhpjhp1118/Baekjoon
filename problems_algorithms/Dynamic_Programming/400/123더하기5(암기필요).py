# https://www.acmicpc.net/problem/15990
import sys
result = [[0, 0, 0] for _ in range(100001)]

# 마지막에 1을 더한 경우, 2를 더한 경우, 3을 더한 경우 각각의 갯수들
result[1] = [1, 0, 0]
result[2] = [0, 1, 0]
result[3] = [1, 1, 1]
# n=3 --> 1+2, 2+1, 3

t = int(sys.stdin.readline().strip())
n_prev = 4
for _ in range(t):
    n = int(sys.stdin.readline().strip())

    for i in range(n_prev, n+1):
        # !!숫자가 너무 크면 계산이 오래걸리므로, 중간값들을 각각 1000000009로 나눈 나머지로 변환한다.
        result[i][0] = result[i-1][1]%1000000009 + result[i-1][2]%1000000009
        result[i][1] = result[i-2][0]%1000000009 + result[i-2][2]%1000000009
        result[i][2] = result[i-3][0]%1000000009 + result[i-3][1]%1000000009
    n_prev = max(n, n_prev)
    print(sum(result[n])%1000000009)

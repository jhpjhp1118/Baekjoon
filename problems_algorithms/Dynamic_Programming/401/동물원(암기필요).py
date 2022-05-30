# https://www.acmicpc.net/problem/1309
import sys

n = int(sys.stdin.readline().strip())
mod = 9901
# 점화식 설명
# https://hooongs.tistory.com/151
# 점화식: result[i] = result[i-1] + 2*result[i-2] + (result[i-1] - result[i-2])
#                   = 2*result[i-1] + result[i-2]

# n = 0 일 땐 경우의 수 1개
# n = 1 일 땐 경우의 수 3개
result = [1, 3] + [0]*(n - 1)

for i in range(2, n + 1):
    result[i] = (2*result[i-1] + result[i-2])%mod

print(result[n])

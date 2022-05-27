# https://www.acmicpc.net/problem/2225
import sys
# <규칙 유도>
# 1) result[n][k] = result[n][k-1] + result[n-1][k-1] + ... + result[1][k-1] + result[0][k-1]
# 1번 식에서, n --> n-1 을 대입하면,
# 2) result[n-1][k] = result[n-1][k-1] + result[n-2][k-1] + ... + result[1][k-1] + result[0][k-1]
# 1번 식에 2번 식을 대입하면,
# result[n][k] = result[n][k-1] + result[n-1][k]

n, k = map(int, sys.stdin.readline().strip().split())
mod = 1000000000

result = [[0]*201 for i in range(201)]

# result[n][k] = result[n-1][k] + result[n][k-1]
# 초기화
for i in range(1, 201):
    result[i][1] = 1 # n 자신을 1번만 더하는 경우
    result[i][2] = i + 1 # (어떤 값), (n-어떤 값) 2개의 수를 더하는 경우
    result[1][i] = i # k개의 (0 or 1)값들 중, 1의 위치만 바꾼 경우

# 점화식 진행
for i in range(2, n+1):
    for j in range(2, k+1):
        result[i][j] = (result[i-1][j] + result[i][j-1])%mod

print(result[n][k])

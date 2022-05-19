# https://www.acmicpc.net/problem/1912
n = int(input())

arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]

# (배열의 현재값) vs. (직전 최대값 + 배열의 현재값) 중 더 큰 걸 기록해간다.
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))
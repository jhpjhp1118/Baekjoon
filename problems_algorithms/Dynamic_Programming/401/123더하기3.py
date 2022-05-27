# https://www.acmicpc.net/problem/15988
import sys

mod = 1000000009
t = int(sys.stdin.readline().strip())

result = [0, 1, 2, 4]

for i in range(t):
    n = int(sys.stdin.readline().strip())

    for j in range(len(result), n+1):
        result.append((result[j-1] + result[j-2] + result[j-3])%mod)
    print(result[n])
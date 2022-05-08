# https://www.acmicpc.net/problem/15990
import sys

# n의 경우의 수는,
#

result = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]
# n=3 --> 1+2, 2+1, 3

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())

    for i in range(len(result), n+1):
        end1 = result[i-1][1] + result[i-2][2]
        end2 = result[i-2][0] + result[i-2][2]
        end3 = result[i-3][0] + result[i-2][1]
        result.append([end1, end2, end3])
    print(sum(result[n])%1000000009)



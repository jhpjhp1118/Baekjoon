# https://www.acmicpc.net/problem/2193
import sys

# 0으로 끝나는 경우 / 1로 끝나는 경우
result = [[0]*2 for _ in range(91)]
result[1] = [0, 1]
for i in range(2, 91):
    # i 개의 자릿수를 가지면서 & 0으로 끝나는 경우 --> i-1개 자릿수의 모든 경우의 끝에 0을 추가하면 됨.
    result[i][0] = sum(result[i-1])
    # i 개의 자릿수를 가지면서 & 1로 끝나는 경우 --> i-1개 자릿수에서 0으로 끝나는 경우의 끝에 1을 추가하면 됨.
    result[i][1] = result[i-1][0]

n = int(sys.stdin.readline().strip())

print(sum(result[n]))


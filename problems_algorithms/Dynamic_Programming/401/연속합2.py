# https://www.acmicpc.net/problem/13398
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))

result = [0]*n
result[0] = data[0]

flag = 0
for i in range(1, n):
    # if flag == 0:
    #     result[i] = max(result[i-1] + data[i], data[i], result[i-1])
    # else:
    #     result[i] = max(result[i - 1] + data[i], data[i])
    result[i] = max(result[i - 1] + data[i], data[i], result[i - 1])
    # if data[i] != 0 and result[i] == result[i-1]:
    #     flag = 1

print(max(result))
# https://www.acmicpc.net/problem/2156
import sys
n = int(sys.stdin.readline().strip())

data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

result = [data[0]]

for i in range(1, n):
    if i == 1:
        result.append(data[0] + data[1])
    elif i == 2:
        result.append(max(data[0] + data[1], data[1] + data[2], data[0] + data[2]))
    else:
        result.append(max(result[i-3] + data[i-1] + data[i], result[i-2] + data[i], result[i-1]))

print(result[n-1])

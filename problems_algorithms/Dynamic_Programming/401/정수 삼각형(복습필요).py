# https://www.acmicpc.net/problem/1932
import sys

n = int(sys.stdin.readline().strip())

data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

# 핵심: 각 data 칸 하나하나 마다, 가능한 최대합을 기록해간다.
# data 와 동일한 형태로 result 를 초기화한다.
result = [[0]*(i+1) for i in range(n)]
result[0][0] = data[0][0]

# n = 1 인 경우를 대비해, 조건을 달아준다.
if n > 1:
    result[1][0] = result[0][0] + data[1][0]
    result[1][1] = result[0][0] + data[1][1]

# 각 row를 탐색한다.
for i in range(2, n):
    for j in range(i + 1):
        if j == 0: # 한 row에서, 가장 왼쪽 값일 때 --> 맨 왼쪽 값들만 계속 더해온 값을 기록한다.
            result[i][0] = result[i-1][0] + data[i][0]
        elif j == i: # 한 row에서, 가장 오른쪽 값일 때 --> 맨 왼쪽 값들만 계속 더해온 값을 기록한다.
            result[i][i] = result[i - 1][i - 1] + data[i][i]
        else: # 한 row에서, 사이에 위치한 값일 때 --> 바로 위의 결과값 2개 중, 더 큰 것을 계속 더해온 값을 기록한다.
            result[i][j] = data[i][j] + max(result[i - 1][j - 1], result[i - 1][j])

# 결과값의 마지막 row에서, 가장 큰 값을 출력한다.
print(max(result[n - 1]))

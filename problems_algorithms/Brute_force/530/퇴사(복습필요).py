# https://www.acmicpc.net/problem/14501
import sys

n = int(sys.stdin.readline().strip())
t = [0]*n
p = [0]*n
for i in range(n):
    t[i], p[i] = list(map(int, sys.stdin.readline().strip().split()))

# [dynamic programming]
result = [[0]*n for _ in range(2)]
# 1번째 줄: i번째 날부터 일을 한다고 했을 때, 얻을 수 있는 최대 보수 합
# 2번째 줄: 더해준 맨 첫 일감의 시작 날짜 (아직 아무 일감도 더해주지 않았으면, -1을 기록한다)
# 일단 result의 마지막 값을 채워준다.
if t[-1] == 1:
    result[0][-1] = p[-1]
    result[1][-1] = n-1
else:
    result[0][-1] = 0
    result[1][-1] = -1

# 마지막 날부터 탐색한다. <-- i번째 날부터 퇴사 할때까지 벌 수 있는 최대 비용을 기록해나간다.
for i in range(n-2, -1, -1):
    # i번째 날 기준으로, 일감의 종료 시점이 퇴사날을 넘어가는 경우
    if i + t[i] > n:

        if result[0][i+1] == 0:
            result[1][i] = -1
        else:
            result[1][i] = result[1][i+1]

        result[0][i] = result[0][i + 1]
    # i번째 일감의 종료 시점이 result[1][i+1]의 맨 처음 일감 날짜와 겹치지 않는 경우
    # or 아직 아직 최대 비용 합이 0이면서 i번재 일감을 수행 가능할 경우
    elif i + t[i] <= result[1][i+1] or result[1][i+1] == -1:
        result[0][i] = result[0][i+1] + p[i]
        result[1][i] = i

    # i번재 일감의 종료 시점이 딱 퇴사날인 경우
    elif i + t[i] == n:
        if p[i] > result[0][i+1]:
            result[0][i] = p[i]
            result[1][i] = i
        else:
            result[0][i] = result[0][i + 1]
            result[1][i] = result[1][i + 1]
    # i번째 일감의 종료 시점이 result[1][i+1]의 맨 처음 일감 날짜와 겹치는 경우
    else:
        if result[0][i+t[i]] + p[i] > result[0][i+1]:
            result[0][i] = result[0][i+t[i]] + p[i]
            result[1][i] = i
        else:
            result[0][i] = result[0][i+1]
            result[1][i] = result[1][i+1]


print(result[0][0])

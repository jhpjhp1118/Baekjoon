# https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

"""
아이디어: 고를 수 있는 회의 일정 중, 회의 끝나는 시간이, 자유시간의 시작점과 가장 가까운 것을 계속 골라나간다.
"""

n = int(input().strip())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().strip().split())))

# 회의 일정을, 끝나는 시간 기준으로 오름차순 정렬한 뒤, 그 안에서 시작 시간 기준으로 오름차순 정렬한다.
data = sorted(data, key=lambda x: (x[1], x[0]))

# 고를 수 있는 회의의 시작 시간 (즉, startTime 이상의 시작 시간을 가진 회의 일정만 고를 수 있다)
startTime = 0
ans = 0
# 모든 일정에 대해 탐색한다.
for time in data:
    # 미리 정렬했으므로, 고를 수 있는 회의기만 하면, 최적의 일정이다. --> 바로 일정에 추가한다.
    if time[0] >= startTime:
        # startTime <-- 추가한 일정의 끝나는 시간 으로 갱신한다.
        startTime = time[1]
        ans += 1

print(ans)



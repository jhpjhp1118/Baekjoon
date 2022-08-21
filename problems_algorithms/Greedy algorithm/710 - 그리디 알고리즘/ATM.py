# https://www.acmicpc.net/problem/11399
import sys

input = sys.stdin.readline

n = int(input().strip())
data = list(map(int, input().strip().split()))
# 걸리는 시간을 오름차순으로 정렬한다.
data = sorted(data)

ans = 0
now = 0 # 현재까지 걸린 시간
for d in data:
    # 현재 시간을 갱신해준다.
    now += d
    # 현재까지 걸린 시간을 더해간다.
    ans += now

print(ans)

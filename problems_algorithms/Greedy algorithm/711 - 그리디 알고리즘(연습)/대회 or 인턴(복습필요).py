# https://www.acmicpc.net/problem/2875
import sys

input = sys.stdin.readline

n, m, k = list(map(int, input().strip().split()))

# 인턴 수를 고려하지 않은 (남녀 인원만 고려한) 최대 팀 수를 구한다.
numTeam = min(n//2, m)
# 그 때 확보되는 인턴 수도 구한다.
numIntern = (n - 2 * numTeam) + (m - numTeam)

# 만약 현재 인턴 수가 요구량보다 적고, 남녀 인원만 고려한 팀 수가 0보다 크다면,
if numIntern < k and numTeam > 0:
    # (요구량 - 현재 인턴 수)가 3으로 나눠 떨어지면, 그 몫만큼 팀을 해체하고 인턴에 채워넣는다.
    if (k - numIntern) % 3 == 0:
        numTeam -= ((k - numIntern) // 3)
    # (요구량 - 현재 인턴 수)가 3으로 나눠 떨어지지 않으면, (그 몫 + 1)만큼 팀을 해체하고 인턴에 채워넣는다.
    else:
        numTeam -= ((k - numIntern) // 3 + 1)

print(numTeam)



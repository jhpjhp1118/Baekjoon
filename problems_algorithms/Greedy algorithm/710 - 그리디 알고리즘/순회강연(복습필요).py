# https://www.acmicpc.net/problem/2109
import sys
import heapq
input = sys.stdin.readline

"""
아이디어: 기본적으로 "보석 도둑" 과 유사함
        강의를 할 수 있는 가장 마지막 날부터 탐색해서, 그날그날에 할 수 있는 가장 비싼 강의만 해가면 된다.
"""

n = int(input().strip())

# 강의를 담아둘 heapq 생성
lecture = []
dayMax = 0 # 강의를 할 수 있는 가장 마지막 날
for _ in range(n):
    p, d = list(map(int, input().strip().split()))
    dayMax = max(dayMax, d) # dayMax를 갱신한다.
    # 가장 나중에 할 수 있는 강의가 맨 앞으로 오도록 heapq에 강의정보를 추가한다.
    heapq.heappush(lecture, [-d, p])

# 현재 갈 수 있는 모든 강의를 기록해둘 heapq 생성한다.
possible = []
ans = 0
# 강의를 할 수 있는 가장 마지막 날부터 반대로 탐색한다.
for day in range(dayMax, 0, -1):
    # 해당 날에 할 수 있는 모든 강의를 기록해둔다. (가장 비싼 강의가 맨 앞으로 오도록)
    while lecture and day <= -lecture[0][0]:
        heapq.heappush(possible, -heapq.heappop(lecture)[1])
    # 하나라도 갈 수 있는 강의가 있다면, 가장 비싼 강의료를 더한다.
    # (남은 강의들은 당연히 다음 탐색하는 날에도 갈 수 있다 <-- 마지막 날부터 거꾸로 탐색중이므로)
    if possible:
        ans -= heapq.heappop(possible)
    # 갈 수 있는 강의가 없고, 남은 강의도 전혀 없다면, 탐색을 종료한다.
    elif not lecture:
        break

print(ans)


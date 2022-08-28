# https://www.acmicpc.net/problem/1202
import sys
import heapq

input = sys.stdin.readline

"""
아이디어: 가장 작은 가방부터 용량 오름차순으로 탐색해서, 넣을 수 있는 가장 비싼 보석을 차례차례 넣어가면 된다.
heapq 특징) 
            1. pop, push를 한 뒤에 바로 첫번째 성분 기준, 오름차순이 됨 (0번째 값이 가장 작고, 마지막 값이 가장 큼)
            2. pop을 하면, 가장 작은 0번째 값이 튀어나옴
"""

n, k = list(map(int, input().strip().split()))

# jewel[i][0]: i번째 보석의 무게 / jewel[i][1]: i번째 보석의 가격
jewel = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().strip().split())))

bags = []
for _ in range(k):
    bags.append(int(input().strip()))
# 가방을 용량 오름차순으로 정렬한다.
bags.sort()

# 현재 가방에 담을 수 있는 보석들을 기록해두기 위한 heapq 생성
possible = []
ans = 0
# 가장 작은 가방부터 차례로 탐색한다.
for bag in bags:
    # 현재 가방이 담을 수 있는 보석을 전부 기록해간다. (가격 내림차순으로)
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(possible, -heapq.heappop(jewel)[1])
    # 현재 가방에 넣을 수 있는 보석이 하나라도 있다면, 가능한 가장 비싼 보석을 현재 가방에 담는다.
    # (possible에 남아있는 보석들은 전부, 다음 가방에도 당연히 넣을 수 있다. <-- 작은 가방부터 차례로 탐색하므로)
    if possible:
        ans -= heapq.heappop(possible)
    # 현재 가방에 넣을 수 있는 보석이 없고, 남은 보석도 전혀 없으면, 탐색을 종료한다.
    # (현재 가방에 넣을 수 있는 보석이 없더라도, 남은 보석이 있으면 탐색을 더 할 수 있다.)
    elif not jewel:
        break

print(ans)



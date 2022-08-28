# 자주쓰고, 같은 의미지만 더 효율적인 코드들 모음

######################
# 숫자 입력 받기
# n = int(input())
import sys

n = int(sys.stdin.readline())

# sys.stdin.readline() 을 쓰면, 마지막에 개행문자 '\n'이 붙게 됨 --> 제거 필요
# 제거법: sys.stdin.readline().strip()

######################
# 리스트를 깊은 복사할 때는, copy.deepcopy 보단, myList[:] 이 더 빠름

######################
# 항상 첫 값이 최소값이어야 하는 자료형이 필요할 땐, heapq를 추천한다.
import heapq

q = []
heapq.heappush(q, 100)
heapq.heappush(q, 10)
heapq.heappush(q, 1)
# q: [1, 100, 10]
heapq.heappop(q) # --> 1 을 내보냄. q: [10, 100] (다시 크기순으로 정렬됨)

######################
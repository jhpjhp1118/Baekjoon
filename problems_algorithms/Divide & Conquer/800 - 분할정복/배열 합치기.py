# https://www.acmicpc.net/problem/11728
import sys

input = sys.stdin.readline

"""
아이디어: merge sort의 그룹 2개를 병합하는 과정을 그대로 가져왔다.
"""

n, m = list(map(int, input().strip().split()))

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

ia = 0 # 리스트 a에서의 index
ib = 0 # 리스트 b에서의 index
il = 0 # 최종 결과에서의 리스트

# 최종 결과리스트 초기화
l = [0]*(n+m)

# ia, ib 둘 다 각 그룹 index 범위 안에 있을 때, a[ia] vs. b[ib] 중 더 작은 것을 계속 채워넣는다
while ia < n and ib < m:
    if a[ia] < b[ib]:
        l[il] = a[ia]
        ia += 1

    else:
        l[il] = b[ib]
        ib += 1

    il += 1

# ia, ib 중 하나라도 그룹 index 범위를 벗어났을 때, (즉 하나의 그룹이라도 모든 성분이 채워넣어졌을 때)
# 남은 성분을 다 채운다.
# a 성분이 남았을 경우
while ia < n:
    l[il] = a[ia]
    ia += 1
    il += 1
# b 성분이 남았을 경우
while ib < m:
    l[il] = b[ib]
    ib += 1
    il += 1

print(*l)
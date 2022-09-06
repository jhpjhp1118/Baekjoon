# https://www.acmicpc.net/problem/12970
import sys

input = sys.stdin.readline

"""
아이디어: 모든 문자를 B로 구성한 것으로 시작해서, (A를 오른쪽에 하나 넣은 뒤, 1칸씩 왼쪽으로 움직이기)를 반복하며, 
        조건을 만족하는 경우를 찾는다.
참고 링크: https://dreamtreeits.tistory.com/139
"""

n, k = list(map(int, input().strip().split()))

# 모든 문자를 B로 초기화한다.
s = list("B" * n)
# 현재 A의 개수 / 현재 (A,B)순서쌍의 개수 / 현재 다루는 A의 index 를 초기화한다.
cntA, currK, idxA = 0, 0, -1

# currK가 목표 k 값과 동일해질 때까지 반복한다.
while currK < k:
    # 새로운 A 추가하기.
    if idxA <= cntA - 1:
        # currK가 최대일 때, 탐색을 종료한다.(절반 지점까지 A가 꽉차면, 그때의 currK가 최대이다.)
        if s[n - 1 - (cntA + 1)] == "A":
            break

        # 지금까지 나온 currK보다 큰 값이 나올 수 있는 자리에 A를 추가한다.
        s[n - 1 - (cntA + 1)] = "A"
        idxA = n - 1 - (cntA + 1)
        currK += 1
        cntA += 1

        
    # 추가한 A를 왼쪽으로 움직이면서 currK 갱신하기.
    else:
        # 기존 A 위치에 B를 채우고, 바로 왼쪽 칸에 A를 채운다.
        s[idxA] = "B"
        s[idxA - 1] = "A"
        idxA -= 1
        currK += 1

if currK == k:
    print(*s, sep="")
else:
    print(-1)

# https://www.acmicpc.net/problem/12015
import sys
input = sys.stdin.readline

"""
아이디어: 이분 탐색을 이용해서, LIS (Longest Increasing Subsequence) 를 찾아준다.
    - 최종적으로 구해진 LIS는, 실제 LIS와는 성분이 다를 수 있다.
        - 이분 탐색 과정에서 계속, 새롭게 등장하는 수 (=case) 를 LIS 리스트 내의 최적의 위치에 갱신시켜주기 때문
    - 원래 Dynamic programming으로 풀 수는 있으나, 계산 복잡도가 O(n^2)으로 오래 걸린다
        - 이분 탐색 자체의 계산 복잡도는 O(logn) 이므로, 이 방법의 계산 복잡도는 O(nlogn) 이다.
"""

n = int(input())
cases = list(map(int, input().split()))
lis = [0]

for case in cases:
    # 수열의 끝 값보다 큰 값이 나오면, 그것을 수열의 끝에 추가한다. (수열 길이 +1)
    # (결국 LIS 길이를 유의미하게 늘리는 건 오직 이부분!)
    if lis[-1]<case:
        lis.append(case)
    # 수열의 끝 값보다 작은 값이 나오면, 그것을 lis 리스트 내 최적의 위치에 추가한다.
    # 최적의 위치: (case 보다 바로 하나 작은 값)의 바로 뒤 --> 기존에 있던 값은 없앤다.
    else:
        # 이분 탐색 구간의 왼쪽 끝, 오른쪽 끝을 정의한다. (이들은 탐색 과정에서 계속 움직인다)
        left = 0
        right = len(lis)
        # left 와 right 가 교차할 때까지 반복한다. (교차 지점이, case의 최적 위치가 된다)
        while left < right:
            # 구간의 가운데 지점을 정의한다.
            mid = (right+left)//2
            # 가운데 지점의 값이 case 보다 작으면, 구간의 왼쪽 끝을 (가운데 지점 + 1)으로 변경한다.
            if lis[mid] < case:
                left = mid + 1
            # 가운데 지점의 값이 case 보다 크면, 구간의 오른쪽 끝을 가운데 지점으로 변경한다.
            else:
                right = mid
        # 최적의 위치의 값을 case로 갱신해준다.
        lis[right] = case

print(len(lis)-1)

"""
공부용 예시

10
100 50 70 90 75 87 105 78 110 60
답: 6
"""

# https://www.acmicpc.net/problem/10973
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n - 1, 0, -1): # 배열의 끝 성분부터 거꾸로 탐색한다.
    if arr[i-1] > arr[i]: # 만약 연속된 두 성분 중, "앞의 성분"이 더 크다면, 
        for j in range(n - 1, i - 1, -1): # 다시 "앞의 성분" 과 배열의 끝 성분부터 거꾸로 비교한다
            if arr[i-1] > arr[j]: # 만약 "앞의 성분" 보다 "작은 성분"을 발견하면,
                arr[i-1], arr[j] = arr[j], arr[i-1] # 그 성분과 서로 swap한다.
                arr = arr[:i] + sorted(arr[i:], reverse=True) # "앞의 성분"까지의 리스트에, 뒤쪽 나머지 리스트는 역정렬한 상태로 이어 붙인다.
                print(*arr)
                exit() 
# 만약 위의 조건을 만족하는 경우가 한번도 안나왔다면, 이는 마지막 순열이다.
print(-1)


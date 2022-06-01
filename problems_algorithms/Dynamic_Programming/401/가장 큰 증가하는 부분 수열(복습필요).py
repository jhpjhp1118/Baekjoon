# https://www.acmicpc.net/problem/11055
import sys

n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

result = [0 for _ in range(n)]

# A의 i번째 성분이 마지막 성분인, 가능한 가장 큰 부분 수열의 수열합을 차례대로 기록해간다.
for i in range(n):
    # i-1 성분까지 탐색한다.
    for j in range(i):
        # 부분 수열의 마지막 성분이 A[i]보다 작은 부분 수열 중, 가장 큰 수열합을 찾는다.
        if A[j] < A[i] and result[j] > result[i]:
            result[i] = result[j]
    # 그 부분 수열의 마지막에 A[i]를 추가하고, 그 값을 수열합에 합친다.
    result[i] += A[i]

print(max(result))

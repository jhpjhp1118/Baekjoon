# https://www.acmicpc.net/problem/11053
import sys

n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

result = [0 for _ in range(n)]

# A의 i번째 성분이 마지막 성분인, 가능한 가장 긴 부분 수열의 길이를 차례대로 기록해간다.
for i in range(n):
    # i-1 성분까지 탐색한다.
    for j in range(i):
        # 부분 수열의 마지막 성분이 A[i]보다 작은 부분 수열 중, 가장 긴 길이를 찾는다.
        if A[j] < A[i] and result[j] > result[i]:
            result[i] = result[j]
    # 그 부분 수열의 마지막에 A[i]를 추가하고, 길이를 +1 한다.
    result[i] += 1

print(max(result))

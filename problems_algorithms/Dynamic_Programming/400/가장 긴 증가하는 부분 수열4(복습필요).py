# https://www.acmicpc.net/problem/14002
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

# 가장 긴 부분 수열 출력하기
# 가장 긴 부분 수열의 마지막 성분 index 찾기
max_idx = result.index(max(result))
# 그 마지막 성분 기록해두기
seq = [A[max_idx]]
# 그 index도 기록해두기
prev_idx = max_idx
# 길이 = (가장 긴 길이-1) ~ 길이 = 1 이 될 때까지 탐색한다.
for i in range(max(result) - 1, 0, -1):
    # 직전에 추가된 성분의 index 의 바로 왼쪽 성분부터 ~ 왼쪽으로 1칸씩 A[j]를 탐색한다.
    for j in range(prev_idx - 1, -1, -1):
        # A[j]를 마지막 성분으로 가지는 부분 수열의 길이가 i이고 & 그 마지막 성분이 seq의 맨 왼쪽 성분보다 작은, A 리스트 상의 index 기록하기
        if result[j] == i and A[j] < A[prev_idx]:
            idx = j
            break
    seq.insert(0, A[idx])
    prev_idx = idx
print(*seq)

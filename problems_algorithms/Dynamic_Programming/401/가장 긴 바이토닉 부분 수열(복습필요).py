# https://www.acmicpc.net/problem/11054
import sys
n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
A_reverse = A[::-1]

increase = [0 for _ in range(n)]
decrease = [0 for _ in range(n)]

# A의 i번째 성분이 마지막 성분인, 가능한 가장 긴 부분 수열의 길이를 차례대로 기록해간다.
for i in range(n):
    # i-1 성분까지 탐색한다.
    for j in range(i):
        # 부분 수열의 마지막 성분이 A[i]보다 작은 부분 수열 중, 가장 긴 길이를 찾는다.
        if A[j] < A[i] and increase[j] > increase[i]:
            increase[i] = increase[j]

    # 그 부분 수열의 마지막에 A[i]를 추가하고, 길이를 +1 한다.
    increase[i] += 1

# A_reverse의 i번째 성분이 마지막 성분인, 가능한 가장 긴 부분 수열의 길이를 차례대로 기록해간다.
for i in range(n):
    # i-1 성분까지 탐색한다.
    for j in range(i):
        # 부분 수열의 마지막 성분이 A[i]보다 큰 부분 수열 중, 가장 긴 길이를 찾는다.
        if A_reverse[j] < A_reverse[i] and decrease[j] > decrease[i]:
            decrease[i] = decrease[j]
    decrease[i] += 1
# decrease 리스트를 뒤집는다. <-- A_reverse 순서대로 기록되었기 때문
decrease.reverse()
# (두 리스트의 각각 대응되는 값을 더한 것 - 1) 중 가장 큰 값을 출력한다.
# -1을 하는 이유: i번째 값이 1번 중복되므로
print(max([increase[i] + decrease[i] for i in range(n)]) - 1)


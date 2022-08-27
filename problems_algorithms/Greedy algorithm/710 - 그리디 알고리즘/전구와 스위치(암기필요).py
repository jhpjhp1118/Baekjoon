# https://www.acmicpc.net/problem/2138
import sys
import copy
input = sys.stdin.readline

"""
참고 링크) https://velog.io/@dding_ji/baekjoon2138
아이디어: 1번째 전구를 바꿀 수 있는 경우 / 바꿀 수 없는 경우로 나눠서 모두 탐색한다.
* 뒤집기 연산을 할지 말지에 대한 기준: 현재 target 전구의 왼쪽 전구가 동일한지 아닌지
    --> target 전구의 왼쪽 전구는, 지금 뒤집기 연산이, 최후의 변경 기회이기 때문.
    (1번째 전구의 경우 예외적으로, A 와 B가 동일한지 & 1번째 전구를 바꾸기로 한 경우인지가 기준이 된다)
* Greedy algorithm 인 이유: 왼쪽에서 오른쪽으로 1번씩만 확인하기 때문

"""

n = int(input().strip())

A = list(map(int, list(input().strip())))
B = list(map(int, list(input().strip())))

v1 = copy.deepcopy(A) # 1번째 전구를 기준으로 뒤집기 연산을 수행하는 경우에 해당하는 A
v2 = copy.deepcopy(A) # 1번째 전구를 기준으로 뒤집기 연산을 수행하지 않는 경우에 해당하는 A

# 뒤집기 연산을 표현한 함수
def reverse(i):
    # 1번째 전구를 기준으로 2개만 뒤집는 경우
    if i == 0:
        A[0] ^= 1
        A[1] ^= 1
    # 마지막 전구를 기준으로 2개만 뒤집는 경우
    elif i == n - 1:
        A[-2] ^= 1
        A[-1] ^= 1
    # 중간의 전구를 기준으로 3개를 뒤집는 경우
    else:
        A[i - 1] ^= 1
        A[i] ^= 1
        A[i + 1] ^= 1

# A 와 B가 동일한지 확인하는 함수
def check():
    for i in range(n):
        if A[i] != B[i]:
            return False

    return True

# v1 과 v2에 대해서 모두 탐색한다.
for j in range(2):
    cnt = 0
    # j 가 0이면 1번째 전구를 뒤집을 수 있고, j가 1이면 1번째 전구를 뒤집을 수 없다.
    A = v1 if j == 0 else v2

    for i in range(n):
        # 1번째 전구
        if i == 0:
            # A가 v1 이고, A 와 B 가 현재 다를 경우, 1번째 전구를 기준으로 뒤집기 연산을 수행한다.
            if j == 0 and not check():
                reverse(i)
                cnt += 1
        # 나머지 전구
        else:
            # 기준이 되는 전구의 왼쪽 전구가 다를 경우, 뒤집는다.
            # (이유: 왼쪽이 되는 전구는, 지금 뒤집기 연산을 하는 것이, 마지막으로 바뀔 수 있는 기회이기 때문)
            if A[i - 1] != B[i - 1]:
                reverse(i)
                cnt += 1
    # A 와 B가 동일하면, cnt 를 출력하고 종료한다
    if check():
        print(cnt)
        exit()
# 탐색이 모두 끝났는데도 A 와 B가 다르면, -1을 출력한다.
print(-1)

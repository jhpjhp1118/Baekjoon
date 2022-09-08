# https://www.acmicpc.net/problem/1201
import sys

input = sys.stdin.readline

"""
아이디어: m, k가 주어져있을 때, 해당 조건을 만족하는 n의 범위는 m + k - 1 <= n <= m * k
        수열을 만들 때, i = 1 부터 시작해서 +1 해가면서... (i: 1부터 차례로 n까지 증가하는 변수 /j: 현재까지 만들어진, 감소 수열 개수)
            - 처음에 k를 만족하는 LDS를 먼저 만들어준다. ([k, k - 1, k - 2, ..., 1]) --> 이 때, i = k, j = 1
            [반복] j 가 m이 될 때까지...
                - ((n - i) // (m - j)) 가 길이인 감소수열을 하나씩 생성해서 붙여준다. --> 이 때, i += ((n - i) // (m - j)), j += 1

        --> 처음에 생성되는 감소수열이 k를 무조건 만족하고, 생성된 감소수열의 총 개수가 m이 되어, LIS도 조건을 무조건 만족하게 된다. 

참고링크) https://sujeng97.tistory.com/9
"""

n, m, k = list(map(int, input().strip().split()))

# n이 불가능한 길이면, 프로그램을 종료한다.
if n < m + k - 1 or n > m * k:
    print(-1)
    exit() 

ans = [x for x in range(k, 0, -1)] # LDS 로 초기화한다.
i = k # 1부터 차례로 n까지, 현재까지 사용한 숫자
j = 1 # 현재까지 만들어진, 감소 수열 개수

# m개의, 적절한 길이의 감소수열을 만들어서 추가한다.
while j < m:
    # 감소수열의 길이를 계산한다.
    length = (n - i) // (m - j)
    # 계산한 길이의 감소수열을 ans에 추가한다.
    ans.extend([x for x in range(i + length, i, -1)])
    i += length
    j += 1 

print(*ans)



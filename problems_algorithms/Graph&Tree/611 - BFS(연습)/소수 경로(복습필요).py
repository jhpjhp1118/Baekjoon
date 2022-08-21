# https://www.acmicpc.net/problem/1963
import sys
from collections import deque
input = sys.stdin.readline

"""
아이디어: "레이저 통신"처럼, 하나의 자리수만 바꾸는 모든 경우를, 차례대로 탐색한다.
ex) 천의 자리만 쭉 --> 십의 자리만 쭉 --> ...
"""

# 주어진 num이 소수인지 판단하는 함수
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 미리 4자리 수들(1000 ~ 9999)의 소수인지 아닌지 여부 판단해놓기 (에라스토테네스의 체 사용)
prime = [False]*9000
for num in range(1000, 10000):
    if isPrime(num):
        prime[num - 1000] = True


t = int(input().strip())

# 각 자리수별로 +/- 2가지 경우의 변화가 가능하다.
steps = [1, -1, 10, -10, 100, -100, 1000, -1000]

def bfs():
    start, end = list(map(int, input().strip().split()))
    # 방문 여부를 표현할 리스트 생성. (1000~9999)
    visited = [False] * 9000
    visited[start - 1000] = True

    q = deque()
    q.append(start)

    ans = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            # 목표값일 경우, 이동 횟수를 출력하고 리턴한다.
            if now == end:
                print(ans)
                return
            for step in steps:
                new = now + step
                while True:
                    # step을 더하기 전 숫자에서, step에 해당하는 자리수의 값
                    digit = ((new - step) // abs(step)) % 10
                    # 해당 자리수를 끝까지 바꿨거나, 새로운 값이 4자리 수가 아닐 경우, 탐색을 종료한다.
                    if (step < 0 and digit == 0) or (step > 0 and digit == 9) or new < 1000 or new >= 10000:
                        break
                    # 만약 new가 소수가 아니거나, 이미 방문했던 소수라면, 해당 숫자는 skip하면서, step만큼 한번 더 더해준다.
                    if not prime[new - 1000] or visited[new - 1000]:
                        new += step
                        continue

                    q.append(new)
                    visited[new - 1000] = True # 해당 new 값의 방문 여부를 기록한다.
                    # step 만큼 쭉 더해나간다.
                    new += step
        ans += 1
    # 탐색이 완전 종료되버린 경우, 접근이 불가능하다는걸 표시해준다.
    print("Impossible")
    return

# 주어진 test case들에 대해 bfs 함수 각각 적용한다.
for _ in range(t):
    bfs()



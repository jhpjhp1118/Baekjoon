# https://www.acmicpc.net/problem/1080
import sys
input = sys.stdin.readline

"""
참고링크: https://jokerldg.github.io/algorithm/2021/03/14/matrix.html
아이디어: 3*3 filter를 옮겨가면서, 기준 칸의 값이 다를 때마다 뒤집기 연산을 전부 수행한다. 그 뒤, A와 B가 동일한지 확인한다.
이 때, 기준칸은 3*3 filter의 가장 왼쪽 위의 칸이 된다.
"""

n, m = list(map(int, input().strip().split()))

# 행렬 A, B 입력받기
A, B = [], []
for _ in range(n):
    line = list(map(int, list(input().strip())))
    A.append(line)

for _ in range(n):
    line = list(map(int, list(input().strip())))
    B.append(line)

# 뒤집기 연산을 진행하는 함수
def reverse(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            A[i][j] ^= 1

# A 와 B 가 동일한지 확인하는 함수
def check():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False

    return True

# 3*3 뒤집기 연산을 못할 정도로 작은 grid 면, A 와 B가 동일한지 확인해서 알맞는 결과를 출력하고 종료한다.
if n < 3 or m < 3:
    # A와 B가 동일할 경우, 0을 출력하고 종료한다.
    if check():
        print(0)
    # A와 B가 다를 경우, -1을 출력하고 종료한다.
    else:
        print(-1)
    exit()

# 뒤집기 연산 횟수
cnt = 0
# (0, 0) ~ (n - 3, m - 3) 사이의 모든 칸을 탐색한다.
for i in range(n - 2):
    for j in range(m - 2):
        # 기준칸(가장 왼쪽 위 칸)의 값이 다를 경우, 3*3 뒤집기 연산을 수행한다.
        if A[i][j] != B[i][j]:
            reverse(i, j)
            cnt += 1

# 탐색이 종료되고 난 후, A 와 B 를 비교해서 알맞는 결과를 출력한다.
# A 와 B 가 동일할 경우, 연산 횟수를 출력한다.
if check():
    print(cnt)
# A 와 B 가 다를 경우, -1 을 출력한다.
else:
    print(-1)




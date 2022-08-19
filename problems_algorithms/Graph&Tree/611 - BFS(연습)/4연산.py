# https://www.acmicpc.net/problem/14395
import sys
from collections import deque

input = sys.stdin.readline

"""
주의) https://www.acmicpc.net/board/view/77662

"""

s, t = list(map(int, input().strip().split()))

# 두 숫자가 같은 경우, 0을 출력한고 종료한다.
if s == t:
    print(0)
    exit()

steps = ["*", "+", "-", "/"]

# 취할 수 있는 action을 함수화함.
def action(num, i):
    # *
    if i == 0:
        return num**2
    # +
    elif i == 1:
        return 2 * num
    # -
    elif i == 2:
        return 0
    # /
    elif i == 3:
        return 1

# 방문 여부를 표시하기 위한 set 생성
visited = set()
visited.add(s)
# 방문한 숫자로 도달하기 위한 최소한의 연산을 기록하는 dictionary 생성
symbols = dict()

q = deque()
q.append(s)
symbols[s] = "" # 시작 숫자는 아무런 연산도 필요 없으므로 초기화.

while q:
    now = q.popleft()

    # 현재 숫자가 t와 같으면, 탐색을 종료한다.
    if now == t:
        print(symbols[now])
        exit()
    # 4가지 action에 대해서 탐색한다.
    for i, step in enumerate(steps):
        # 현재 숫자가 0이고, 나눗셈을 해야하는 상황이면, skip 한다.
        if i == 3 and now == 0:
            continue

        num = action(now, i)
        # num이 s, t의 범위를 넘어가거나, 이미 방문한 숫자일 경우, skip 한다.
        if num <= 0 or num > 10 ** 9 or num in visited:
            continue

        visited.add(num) # 방문 여부 표시
        symbols[num] = symbols[now] + step # 연산 기록하기
        q.append(num)
# t 에 도달하지 못하고 탐색이 종료되면, -1을 출력한다.
print(-1)


# https://www.acmicpc.net/problem/12886
import sys
from collections import deque

a, b, c = list(map(int, sys.stdin.readline().strip().split()))

def action(num1, num2):
    # num1 < num2 라고 가정한다.

    n1 = num1 * 2
    n2 = num2 - num1

    return n1, n2

# a b c 가 전부 크기순으로 정렬된 경우만 탐색한다. (*효율*) <-- 해결 가능 여부만 확인하면 되므로
case = tuple(sorted((a, b, c)))
q = deque()
q.append(case)

# 이미 방문했던 case인지 확인하기 위한 set 생성
visited = set()
visited.add(case)

while q:
    nowA, nowB, nowC = q.popleft()
    # 현재의 A, B, C가 모두 동일할 경우, 1을 출력하고 종료한다.
    if nowA == nowB == nowC:
        print(1)
        exit()

    # ! 정렬되어 있으므로, 항상 더 왼쪽에 위치한 수 <= 더 오른쪽에 위차한 수를 만족한다 !
    # ex) A <= B <= C
    # A <--> B
    if nowA != nowB:
        targetA, targetB = action(nowA, nowB)
        case = tuple(sorted((targetA, targetB, nowC)))
        if case not in visited:
            q.append(case)
            visited.add(case)

    # B <--> C
    if nowB != nowC:
        targetB, targetC = action(nowB, nowC)
        case = tuple(sorted((nowA, targetB, targetC)))
        if case not in visited:
            q.append(case)
            visited.add(case)

    # C <--> A
    if nowA != nowC:
        targetA, targetC = action(nowA, nowC)
        case = tuple(sorted((targetA, nowB, targetC)))
        if case not in visited:
            q.append(case)
            visited.add(case)

# 해결하지 못하고 탐색을 종료했을 경우, 불가능이므로 0을 출력한다.
print(0)


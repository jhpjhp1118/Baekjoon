# https://www.acmicpc.net/problem/14888

import sys

N = int(sys.stdin.readline().strip()) # 숫자의 개수
A = list(map(int, sys.stdin.readline().strip().split())) # 숫자들
symbols = list(map(int, sys.stdin.readline().strip().split())) # 연산자들

valMax, valMin = -1e15, 1e15

# 연산자에 따른 연산을 수행한다
def computeVal(val1, val2, symbolIdx):
    if symbolIdx == 0: # 덧셈
        return val1 + val2
    elif symbolIdx == 1: # 뺄셈
        return val1 - val2
    elif symbolIdx == 2: # 곱셈
        return val1*val2
    elif symbolIdx == 3: # 나눗셈
        if val1 >= 0: # 양수를 양수로 나눌 때
            return val1//val2
        else: # 음수를 양수로 나눌 때
            return -(abs(val1)//val2)


def dfs(depth, valCurr, symbolsCurr):
    global valMax, valMin
    # 깊이가 N에 도달하면, valMax & valMin을 갱신하고 해당 가지의 탐색을 종료한다
    if depth == N:
        valMax = max(valCurr, valMax)
        valMin = min(valCurr, valMin)
        return

    # 탐색
    for symbolIdx in range(4):
        # 아직 사용가능한 연산자라면, 더 깊게 탐색한다
        if symbolsCurr[symbolIdx] > 0:
            # 해당 연산자를 넣은 값을 계산한다.
            valNext = computeVal(valCurr, A[depth], symbolIdx)
            symbolsCurr[symbolIdx] -= 1
            # dfs 더 깊게 탐색 들어간다
            dfs(depth=depth + 1, valCurr=valNext, symbolsCurr=symbolsCurr)
            # 해당 연산자를 넣지 않은 값으로 되돌린다
            symbolsCurr[symbolIdx] += 1


dfs(depth=1, valCurr=A[0], symbolsCurr=symbols)

print(valMax, valMin, sep='\n')
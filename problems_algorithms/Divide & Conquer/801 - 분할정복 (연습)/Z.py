# https://www.acmicpc.net/problem/1074
import sys

input = sys.stdin.readline

n, r, c = list(map(int, input().strip().split()))

def dfs(n, r, c, rCurr, cCurr, valCurr):
    if n == 0:
        return valCurr

    print(rCurr, cCurr, valCurr)
    # 해당 그리드에서, 0,1,2,3 사분면 중 어디에 위치하는지 찾는다.
    gridNum = -1
    if r < rCurr + 2**(n - 1):
        if c < cCurr + 2**(n - 1):
            gridNum = 0
        else:
            cCurr = cCurr + 2**(n - 1)
            gridNum = 1
    else:
        rCurr = rCurr + 2 ** (n - 1)
        if c < cCurr + 2**(n - 1):
            gridNum = 2
        else:
            cCurr = cCurr + 2**(n - 1)
            gridNum = 3

    valCurr += gridNum*2**(n - 1)

    print(rCurr, cCurr, valCurr)
    dfs(n - 1, r, c, rCurr, cCurr, valCurr)

print(dfs(n, r, c, 0, 0, 0))

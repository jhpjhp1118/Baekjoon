# https://www.acmicpc.net/problem/1074
import sys

input = sys.stdin.readline

n, r, c = list(map(int, input().strip().split()))

def dfs(n, r, c, rCurr, cCurr, valCurr):
    # 최종적으로 1칸짜리 서브 그리드에 도달하면, 결과값을 출력하고 종료한다.
    if n == 0:
        print(valCurr)
        exit()

    # 해당 그리드에서, 0,1,2,3 사분면 중 어디에 위치하는지 찾는다. 
    # 동시에, rCurr & cCurr 를 갱신한다.
    gridNum = -1
    # row 좌표가 서브 그리드의 절반 row 좌표보다 위에 있을 경우,
    if r < rCurr + 2**(n - 1):
        # col 좌표가 서브 그리드의 절반 col 좌표보다 왼쪽에 있을 경우, --> 0사분면
        if c < cCurr + 2**(n - 1):
            gridNum = 0
        # col 좌표가 서브 그리드의 절반 col 좌표보다 오른쪽에 있을 경우, --> 1사분면
        else:
            cCurr = cCurr + 2**(n - 1)
            gridNum = 1
    # row 좌표가 서브 그리드의 절반 row 좌표보다 아래에 있을 경우,
    else:
        rCurr = rCurr + 2 ** (n - 1)
        # col 좌표가 서브 그리드의 절반 col 좌표보다 왼쪽에 있을 경우, --> 2사분면
        if c < cCurr + 2**(n - 1):
            gridNum = 2
        # col 좌표가 서브 그리드의 절반 col 좌표보다 오른쪽에 있을 경우, --> 3사분면
        else:
            cCurr = cCurr + 2**(n - 1)
            gridNum = 3

    # valCurr를 해당 서브 그리드의 첫칸의 순서로 갱신한다. (gridnum*서브 그리드의 칸 개수 만큼 더해주기)
    valCurr += gridNum*2**(2*(n - 1))

    # 해당 서브 그리드에 대해 재귀호출한다.
    dfs(n - 1, r, c, rCurr, cCurr, valCurr)

dfs(n, r, c, 0, 0, 0)

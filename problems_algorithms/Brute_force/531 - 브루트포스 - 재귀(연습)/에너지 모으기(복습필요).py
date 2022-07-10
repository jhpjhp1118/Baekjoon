# https://www.acmicpc.net/problem/16198
import sys

n = int(sys.stdin.readline().strip())

weights = list(map(int, sys.stdin.readline().strip().split()))

# 초기 순서 기준, 아직 방문하지 않은 구슬을 기록해놓는 리스트 생성
nonVisited = [i for i in range(n)]

nCurr = n # 현재 남은 구슬
global ans
ans = -1

def dfs(nonVisited, nCurr, val):
    global ans
    # 에너지 구슬이 2개만 남았을 경우, 탐색을 종료하고, ans 값을 더 큰 값으로 갱신한다.
    if nCurr == 2:
        ans = max(ans, val)
        return

    # 2번째 구슬 ~ 마지막에서 2번째 구슬까지 탐색한다.
    for i in range(1, nCurr - 1):
        idx = nonVisited[i] # nonVisited에서 제거할 값 확인
        nonVisited.remove(idx) # 해당 값 제거
        # 다음 단계로 탐색한다.
        # 이미 nonVisited에서 값을 하나 제거한 상태이므로, nonVisitied[i - 1], nonVisited[i] 번째 weight들을 곱해서 val에 더해준다.
        dfs(nonVisited, nCurr - 1, val + weights[nonVisited[i - 1]]*weights[nonVisited[i]])
        nonVisited.insert(i, idx) # 제거했던 값 제자리에 되돌려 놓기

dfs(nonVisited, nCurr, 0)
print(ans)

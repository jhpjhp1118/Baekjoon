# https://www.acmicpc.net/problem/15649
import sys

n, m = map(int, sys.stdin.readline().strip().split())

s = []

def dfs():
    # 목표 길이에 도달하면, 탐색을 종료하고 출력한다.
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    # s에 i 성분이 없으면, 추가하고 그 다음 수로 넘어간다. 그 뒤 돌아온다 (= 추가한 i 성분을 뺀다.)
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()


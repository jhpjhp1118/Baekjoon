# https://www.acmicpc.net/problem/15650
import sys

n, m = map(int, sys.stdin.readline().strip().split())

s = []
def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n+1):
        if i not in s:
            # s에 성분이 아예 없거나, s의 마지막 성분이 i보다 작으면, i를 끝에 추가해본다.
            if len(s) == 0 or i > s[-1]:
                s.append(i)
                dfs()
                s.pop()

dfs()

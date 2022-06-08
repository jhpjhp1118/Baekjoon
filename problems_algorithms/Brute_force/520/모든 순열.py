# https://www.acmicpc.net/problem/10974
import sys

n = int(sys.stdin.readline().strip())

s = []
def dfs():
    if len(s) == n:
        print(*s)

    for i in range(n):
        if i + 1 not in s:
            s.append(i + 1)
            dfs()
            s.pop()

dfs()


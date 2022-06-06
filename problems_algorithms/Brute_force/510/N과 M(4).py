# https://www.acmicpc.net/problem/15652
import sys

n, m = map(int, sys.stdin.readline().strip().split())

s = []

def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n+1):
        if len(s) == 0 or i >= s[-1]:
            s.append(i)
            dfs()
            s.pop()

dfs()

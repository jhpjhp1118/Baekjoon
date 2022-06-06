# https://www.acmicpc.net/problem/15655
import sys

n, m = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))
data = sorted(data)

s = []

def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in data:
        if i not in s:
            if len(s) == 0 or i > s[-1]:
                s.append(i)
                dfs()
                s.pop()

dfs()

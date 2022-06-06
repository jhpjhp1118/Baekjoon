# https://www.acmicpc.net/problem/15663
import sys

n, m = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))
data = sorted(data)

s = []
idxs = []
def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i, val in enumerate(data):
        if i not in idxs:
            s.append(val)
            idxs.append(i)
            dfs()
            s.pop()
            idxs.pop()

dfs()

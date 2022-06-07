# https://www.acmicpc.net/problem/15666
import sys

n, m = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))
data = sorted(data)

s = []

def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    overlap = -1 # 현재 자리에서 이미 탐색한 값을 또 탐색하는 것을, 방지하기 위함
    for i, val in enumerate(data):
        if overlap != val and (len(s) == 0 or s[-1] <= val):
            s.append(val)
            overlap = val
            dfs()
            s.pop()

dfs()

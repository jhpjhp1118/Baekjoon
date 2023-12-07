import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

def dfs(s):
    if len(s) == m:
        print(' '.join(list(map(str, s))))
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs(s)
            s.pop()


dfs(s=[])
# https://www.acmicpc.net/problem/2178
import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

maze = []
for _ in range(n):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

visited = [False]*(n*m)

def dfs():
    if r == n and c == m:

        return



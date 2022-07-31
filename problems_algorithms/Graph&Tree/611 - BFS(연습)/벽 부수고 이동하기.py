# https://www.acmicpc.net/problem/2206
import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

maze = []
for i in range(n):
    line = list(map(int, list(input().strip())))
    maze.append(line)

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]



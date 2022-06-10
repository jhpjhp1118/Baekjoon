# https://www.acmicpc.net/problem/14501
import sys

n = int(sys.stdin.readline().strip())
t = [0]*n
p = [0]*n
for i in range(n):
    t[i], p[i] = list(map(int, sys.stdin.readline().strip().split()))




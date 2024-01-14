# https://www.acmicpc.net/problem/13458

import sys

n = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().strip().split()))

B, C = list(map(int, sys.stdin.readline().strip().split()))


def isPositive(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1


A = [a - B for a in A]
# a%C 가, 0이면 0, 0보다 크면 1
refs = [a//C + 1 + isPositive(a%C) if a > 0 else 1 for a in A]

print(sum(refs))

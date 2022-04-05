# https://www.acmicpc.net/problem/9093
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

stack = deque()
for _ in range(n):
    line = sys.stdin.readline().strip()
    line += " "
    for char in line:
        if char != " ":
            stack.append(char)
        else:
            while(stack):
                print(stack.pop(), end="")
            print(" ", end="")
    print()

# https://www.acmicpc.net/problem/1406
import sys
from collections import deque

stack_left = deque(sys.stdin.readline().strip())
stack_right = deque()

n = int(sys.stdin.readline().strip())

for _ in range(n):
    line = sys.stdin.readline().strip().split()

    if line[0] == "L":
        if len(stack_left) == 0: 
            continue
        stack_right.append(stack_left.pop())
    elif line[0] == "D":
        if len(stack_right) == 0:
            continue
        stack_left.append(stack_right.pop())
    elif line[0] == "B":
        if len(stack_left) == 0:
            continue
        stack_left.pop()
    elif line[0] == "P":
        stack_left.append(line[1])


while(stack_right):
    stack_left.append(stack_right.pop())

print("".join(stack_left))
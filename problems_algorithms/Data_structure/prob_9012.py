# https://www.acmicpc.net/problem/9012
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for _ in range(n):
    line = sys.stdin.readline().strip()
    stack = deque()
    flag = 0
    for char in line:
        if char == "(":
            stack.append(1)
        elif char == ")":
            try: 
                stack.pop()
            except:
                flag = 1
                break

    if len(stack) != 0 or flag == 1:
        print("NO")
    else:
        print("YES")
    

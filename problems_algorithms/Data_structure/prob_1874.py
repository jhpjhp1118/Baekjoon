# https://www.acmicpc.net/problem/1874
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

stack = deque()
result = deque()
num = 0
flag = 0
for _ in range(n):
    target = int(sys.stdin.readline().strip())
    while num < target:
        num += 1
        stack.append(num)
        result.append("+")
    
    if stack[-1] == target:
        stack.pop()
        result.append("-")

    else:
        flag = 1
        break
if flag == 1:
    print("NO")
else:
    print("\n".join(result))
    



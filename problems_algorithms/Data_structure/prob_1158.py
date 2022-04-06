# https://www.acmicpc.net/problem/1158
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
que = deque(range(1, n+1))
result = deque()
while(que):
    for _ in range(k-1):
        que.append(que.popleft())
    result.append(que.popleft())

print("<", ", ".join(list(map(str, result))), ">", sep="")

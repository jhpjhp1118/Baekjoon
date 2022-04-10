# https://www.acmicpc.net/problem/17299
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
result = [-1]*n

stack = deque()
dictCount = {}
# 횟수 세서 딕셔너리에 채우기
for num in nums:
    try: dictCount[num] += 1
    except: dictCount[num] = 1

for i, num in enumerate(nums):
    while stack and dictCount[nums[stack[-1]]] < dictCount[num]:
        result[stack.pop()] = num
    stack.append(i)
print(*result)

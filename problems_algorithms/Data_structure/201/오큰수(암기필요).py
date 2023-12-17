# https://www.acmicpc.net/problem/17298
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
result = [-1]*n

stack = deque()

for i, num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        result[stack.pop()] = num
    stack.append(i)

print(*result)

# 처음 index(=0)를 담은 뒤,

# 현재 보고 있는 수 > 직전 수 --> 직전 수의 오큰수는 현재 보고 있는 수
# 현재 보고 있는 수 <= 직전 수 --> 아직 오큰수 아님. 다음 수로 넘어간다.

# stack: 직전 수까지의 index들 잠시 저장
# nums의 숫자를 하나씩 탐색할 때마다, 아직 stack에 남아 있는 값들 중, num 보다 작은게 있는지 확인한다

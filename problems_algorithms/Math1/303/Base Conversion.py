# https://www.acmicpc.net/problem/11576
import sys

a, b = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

# a진법 --> 10진법으로 숫자 바꾸기
power = m - 1
digit = 0
for i in range(m):
    digit += nums[i]*a**power
    power -= 1

# 10진법 --> b진법으로 바꾸기
result = []
while True:
    residual = digit%b

    result.insert(0, residual)
    if digit < b:
        break

    digit //= b

print(*result)
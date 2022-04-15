# https://www.acmicpc.net/problem/10824
import sys

nums = sys.stdin.readline().strip().split()

result = int(nums[0] + nums[1]) + int(nums[2] + nums[3])

print(result)

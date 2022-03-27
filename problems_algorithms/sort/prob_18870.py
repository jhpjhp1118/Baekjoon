# https://www.acmicpc.net/problem/18870
import sys
n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().strip().split()))

nums_sort = sorted(set(nums))

dic = {}
for i, num in enumerate(nums_sort):
    dic[num] = i

for num in nums:
    print(dic[num], end=" ")
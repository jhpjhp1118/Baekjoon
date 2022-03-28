# https://www.acmicpc.net/problem/2798
import sys
n, m = list(map(int, sys.stdin.readline().strip().split()))

nums = list(map(int, sys.stdin.readline().strip().split()))

jack = 0
s = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j < k:
                s = nums[i]+nums[j]+nums[k]
                if jack < s <= m:
                    jack = s
            else:
                continue
print(jack)

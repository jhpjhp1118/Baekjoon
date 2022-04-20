# https://www.acmicpc.net/problem/17087
import sys
import math

n, s = list(map(int, sys.stdin.readline().strip().split()))

nums = list(map(int, sys.stdin.readline().strip().split()))
diff = [abs(s - i) for i in nums]

d = min(diff)
for i in diff:
    d = math.gcd(d, i)
print(d)

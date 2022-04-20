# https://www.acmicpc.net/problem/9613
import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

t = int(sys.stdin.readline().strip())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    n = nums[0]
    result = 0
    for i in range(n):
        for j in range(n):
            if i > j:
                result += gcd(nums[i + 1], nums[j + 1])
    print(result)

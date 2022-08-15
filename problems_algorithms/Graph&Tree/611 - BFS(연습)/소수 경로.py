# https://www.acmicpc.net/problem/1963
import sys

input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 미리 4자리 수들(1000 ~ 9999)의 소수인지 아닌지 여부 판단해놓기 (에라스토테네스의 체 사용)
prime = [False]*9000
for num in range(1000, 10000):
    if isPrime(num):
        prime[num - 1000] = True

t = int(input().strip())

for _ in range(t):
    start, end = list(map(int, input().strip().split()))





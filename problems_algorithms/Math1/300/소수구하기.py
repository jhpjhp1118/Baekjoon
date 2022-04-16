# https://www.acmicpc.net/problem/1929
import sys

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1): # num = 2, 3 일 때는 loop가 하나도 돌지 않아서 True가 리턴됨.
        if num % i == 0:
            return False
    return True

m, n = map(int, sys.stdin.readline().strip().split())

# 에라스토테네스의 체: 하나의 수가 소수인지 판단할 때, 그 수의 제곱근까지만 나눠떨어지는지 확인해보면 된다.
for num in range(m, n+1):# 각 수마다 소수인지 아닌지 판단
    if isPrime(num):
        print(num)






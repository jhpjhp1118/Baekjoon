# https://www.acmicpc.net/problem/6588
import sys

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    line = sys.stdin.readline().strip()
    num = int(line)
    if not line or num == 0:
        break

    prime1, prime2 = 0, 0
    flag = False
    for i in range(1, num//4 + 1):# prime1은 num의 절반보다 작으며, 홀수를 탐색하기 위해 num//4를 사용한다.
        test = 2*i + 1 # 홀수이면서 가장 작은 소수는 3 --> 3부터 차례로 탐색한다.
        if isPrime(test) and isPrime(num - test):
            prime1, prime2 = test, num - test
            flag = True
            break

    if flag:
        print("{num} = {prime1} + {prime2}".format(num=num, prime1=prime1, prime2=prime2))
    else:
        print("Goldbach's conjecture is wrong.")

# n이 주어졌을 때, n/2 보다 작고, 홀수인, 모든 소수를 탐색하면 됨
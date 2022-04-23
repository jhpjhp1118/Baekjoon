# https://www.acmicpc.net/problem/17103
import sys

global check, prime
check = [False, False] + [True] * 1000000

for i in range(2, 1001):
    if check[i] == True:
        for j in range(i + i, 1000001, i):
            check[j] = False

prime = [x for x in range(len(check)) if check[x] == True]


def Goldbach(n):
    if n == 0:
        return 0

    count = 0
    for A in prime:
        if A > n//2:
            break
        B = n - A
        if check[B]:
            count += 1

    return count


t = int(sys.stdin.readline().strip())

for _ in range(t):

    n = int(sys.stdin.readline().strip())
    print(Goldbach(n))


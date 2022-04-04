# https://www.acmicpc.net/problem/11729
import sys

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)


n = int(sys.stdin.readline().strip())
print(2**n - 1)
hanoi(n, 1, 2, 3)
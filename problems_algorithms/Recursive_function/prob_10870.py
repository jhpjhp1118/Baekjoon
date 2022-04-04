# https://www.acmicpc.net/problem/10870
import sys

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(sys.stdin.readline().strip())

print(fibonacci(n))


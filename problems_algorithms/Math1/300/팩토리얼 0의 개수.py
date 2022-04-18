# https://www.acmicpc.net/problem/1676
import sys

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n - 1)

n = int(sys.stdin.readline().strip())
fact_str = str(factorial(n))

count = 0
for i in range(len(fact_str) - 1, 0, -1):
    if fact_str[i] == "0":
        count += 1
    else:
        break

print(count)
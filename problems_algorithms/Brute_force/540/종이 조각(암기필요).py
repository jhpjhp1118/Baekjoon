# https://www.acmicpc.net/problem/14391
import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
# for _ in range(n):
    # arr.append(list(map(int, list(sys.stdin.readline().strip()))))

print(arr)




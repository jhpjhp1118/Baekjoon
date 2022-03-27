# https://www.acmicpc.net/problem/1181
import sys
n = int(sys.stdin.readline())

strs = []
for _ in range(n):
    strs.append(sys.stdin.readline().strip())

strs = set(strs)
strs = sorted(strs, key=lambda x: (len(x), x))

for s in strs:
    print(s)
# https://www.acmicpc.net/problem/11656
import sys

line = sys.stdin.readline().rstrip("\n")

strs = []
for i in range(len(line)):
    strs.append(line[i:])

print("\n".join(sorted(strs)))

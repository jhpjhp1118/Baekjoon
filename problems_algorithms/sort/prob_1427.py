# https://www.acmicpc.net/problem/1427
import sys
line = list(map(int, list(sys.stdin.readline().strip())))

line = sorted(line)[::-1]
for e in line:
    print(e, end="")


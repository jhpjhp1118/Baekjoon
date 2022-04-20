# https://www.acmicpc.net/problem/1373
import sys

s = sys.stdin.readline().strip()
s_10 = int(s, 2)
s_8 = oct(s_10)

print(s_8[2:])


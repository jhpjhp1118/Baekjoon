# https://www.acmicpc.net/problem/1212
import sys

s = sys.stdin.readline().strip()
s_10 = int(s, 8)
s_2 = bin(s_10)

print(s_2[2:])


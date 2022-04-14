# https://www.acmicpc.net/problem/10808
import sys

line = sys.stdin.readline().strip()

num_alpha = [0]*26
a_ascii = ord("a")
for char in line:
    num_alpha[ord(char) - a_ascii] += 1

print(*num_alpha)
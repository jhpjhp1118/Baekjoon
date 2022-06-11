# https://www.acmicpc.net/problem/2529
import sys

n = int(sys.stdin.readline().strip())
bracket = sys.stdin.readline().strip().split()

def compare(brac, num1, num2):
    if brac == ">":
        if num1 > num2:

    else:

def dfs_max(s, brac):
    if len[s] == n:
        print("".join(s))
        return

    for i in range(9, -1, -1):
        if i not in s:



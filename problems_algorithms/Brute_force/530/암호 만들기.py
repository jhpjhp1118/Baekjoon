# https://www.acmicpc.net/problem/1759
import sys

L, C = list(map(int, sys.stdin.readline().strip().split()))
chars = sys.stdin.readline().split()

unicodes = sorted(list(map(ord, chars)))
vowel = list(map(ord, "a e i o u".split()))


def dfs(s):
    if len(s) == L:
        vowelNum = 0
        for v in vowel:
            if v in s:
                vowelNum += 1
        if 1 <= vowelNum <= L - 2:
            print("".join(list(map(chr, s))))
        return
    
    for i in unicodes:
        if i not in s and (len(s) == 0 or s[-1] < i):
            s.append(i)
            dfs(s)
            s.pop()

dfs(s=[])

# https://www.acmicpc.net/problem/2447
import sys
sys.setrecursionlimit(10**6)

def append_star(len):
    if len == 1:
        return ("*")

    stars = append_star(len//3)
    L = []

    for s in stars:
        L.append(s*3)

    for s in stars:
        L.append(s + " "*(len//3) + s)

    for s in stars:
        L.append(s*3)

    return L


n = int(sys.stdin.readline().strip())
print("\n".join(append_star(n)))

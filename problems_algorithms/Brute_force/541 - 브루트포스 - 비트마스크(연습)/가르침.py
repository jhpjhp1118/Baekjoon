# https://www.acmicpc.net/problem/1062
import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))

# a, c, i, n, t --> 최소 5개 알파벳 필요하므로, K가 이보다 적으면 아무것도 읽을 수 없다
if K < 5:
    print(0)
    exit()




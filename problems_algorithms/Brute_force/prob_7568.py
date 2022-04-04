# https://www.acmicpc.net/problem/7568
import sys
n = int(sys.stdin.readline().strip())

data = []
for _ in range(n):
    weight, height = map(int, sys.stdin.readline().strip().split())
    data.append([weight, height])

# 각 person마다, 몇 등인지 일일히 확인한다.
for i in data:
    rank = 1
    for j in data:
        if (i[0] < j[0]) and (i[1] < j[1]):
            rank += 1
    print(rank, end=" ")


# https://www.acmicpc.net/problem/10814
import sys
n = int(sys.stdin.readline())

data = []
for order in range(n):
    line = sys.stdin.readline().strip().split()
    data.append([int(line[0]), line[1], order])

data = sorted(data, key=lambda x: (x[0], x[2]))
for person in data:
    print(person[0], person[1])
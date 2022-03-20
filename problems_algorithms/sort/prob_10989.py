# https://www.acmicpc.net/problem/10989
import sys
n = int(sys.stdin.readline())
num_list = [0]*10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

# for i in num_list:
#     if i != 0:
#         for _ in range(i):
#             print(i)
for i in range(10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)


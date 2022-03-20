# https://www.acmicpc.net/problem/2750
# Time Complexity: O(n^2)
n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

for i in range(len(num)):
    print(num[i], end="\n")
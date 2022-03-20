# https://www.acmicpc.net/problem/2588
a = int(input())
b = list(map(int, list(input())))

x1 = a * b[2]
x2 = a * b[1]
x3 = a * b[0]

out = x1 + x2 * 10 + x3 * 100

print(x1, x2, x3, sep="\n")
print(out)
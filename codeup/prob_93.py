# https://codeup.kr/problem.php?id=6093

n = int(input())
a = input().split()


for i in range(n-1, -1, -1):
    print(a[i], end=" ")
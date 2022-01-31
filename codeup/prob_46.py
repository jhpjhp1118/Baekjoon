# https://codeup.kr/problem.php?id=6046
n = int(input())
n = n << 1 # n을 2배 한 값이 나오게 됨. (2진법 상으로, 왼쪽으로 1칸 옮긴다)
print(n)

# https://codeup.kr/problem.php?id=6047
n, i = map(int, input().split())
n = n << i # n을 2배 한 값이 나오게 됨. (2진법 상으로, 왼쪽으로 1칸 옮긴다)
print(n)
# https://codeup.kr/problem.php?id=6096
# 인풋 grid 입력받기
grid = []
for i in range(19):
    row = list(map(int, input().split()))
    grid.append(row)

# 십자 뒤집기 입력받기 & 반영
# 반영할 때, val = 1 - val 또는 XOR 비트 연산자 ^= 사용
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    # rowInv = [grid[x][j]^1 if j != y else grid[x][j] for j in range(19)]
    # colInv = [grid[j][y]^1 if j != y else grid[j][y] for j in range(19)]
    for j in range(19):
        if j != y:
            grid[x][j] ^= 1
        if j != x:
            grid[j][y] ^= 1

# value 하나씩 출력하기
for i in range(19):
    for j in range(19):
        print(grid[i][j], end=" ")
    print()

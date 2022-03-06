# https://codeup.kr/problem.php?id=6095
grid = [[0 for i in range(19)] for j in range(19)]
# for i in range(len(grid)):
#     print(grid[i], end="\n")

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    grid[x][y] = 1

for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end=" ")
    print()

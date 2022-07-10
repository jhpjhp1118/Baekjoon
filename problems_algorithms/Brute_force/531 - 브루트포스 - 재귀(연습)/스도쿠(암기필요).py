# https://www.acmicpc.net/problem/2580
import sys

"""
아이디어: 모든 빈칸에 대해, 가능한 모든 숫자를 하나씩 채워보면서 dfs로 탐색한다.
참고링크: https://claude-u.tistory.com/360
"""

grid = []

for _ in range(9):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))

# 채워지지 않은 칸들 리스트에 기록해두기
zeros = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]


def get_possible(r, c):
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 직접 입력해서 할당하면, 계산시간 단축됨!! <-- 시간 초과 방지용
    # 행, 열 방면으로 확인하기
    for i in range(9):
        # 열 방면
        if grid[i][c] in possible:
            possible.remove(grid[i][c])
        # 행 방면
        if grid[r][i] in possible:
            possible.remove(grid[r][i])

    # 사각형 확인하기
    y = r // 3
    x = c // 3

    for i in range(3 * y, 3 * y + 3):
        for j in range(3 * x, 3 * x + 3):
            if grid[i][j] in possible:
                possible.remove(grid[i][j])

    return possible


def dfs(idx):
    # 모든 빈 칸들을 채워넣었을 경우, 출력하고 종료한다.
    if idx == len(zeros):
        for row in grid:
            print(*row)
        exit()

    r, c = zeros[idx]
    # (r, c) 에서 가능한 모든 숫자들을 확인한다.
    possible = get_possible(r, c)

    # 가능한 숫자들에 대해, 다음 단계로 탐색한다.
    for num in possible:
        grid[r][c] = num
        dfs(idx + 1)
        grid[r][c] = 0

dfs(0)



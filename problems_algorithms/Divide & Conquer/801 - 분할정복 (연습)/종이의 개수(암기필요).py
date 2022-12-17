# https://www.acmicpc.net/problem/1780
import sys

input = sys.stdin.readline

"""
계산 효율성이 중요하다! 부분 grid 내의 모든 성분이 같은지 확인하는 계산량을 최소화해야 한다.
아이디어: 차례대로 성분을 탐색하며, 다른 성분이 나오면, 바로 재귀호출한다.
"""

n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))

global result
result = {-1:0, 0:0, 1:0} # -1, 0, 1 종이의 개수

def split_grid(row, col, length):
    global result
    # 해당 grid의 첫성분 초기화
    curr = grid[row][col]

    # 부분 grid 범위를 탐색...
    for i in range(row, row + length):
        for j in range(col, col + length):
            # 만약 첫성분과 다른 값을 포함하고 있다면, 9등분하고 재귀호출한다.
            if grid[i][j] != curr:
                # 행렬 길이의 3등분
                small_length = length//3
                # 9개의 작은 grid에 대해 재귀 호출
                for k in range(3):
                    for l in range(3):
                        split_grid(row + k*small_length, col + l*small_length, small_length)
                return
    # 만약 모두 첫성분과 같다면, 해당 성분의 종이 개수를 +1 한다.
    result[curr] += 1

split_grid(0, 0, n)
for num in result.values():
    print(num)


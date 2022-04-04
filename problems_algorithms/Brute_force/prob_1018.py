# https://www.acmicpc.net/problem/1018
import sys
height, width = map(int, sys.stdin.readline().strip().split())

board = []
for _ in range(height):
    board.append(list(sys.stdin.readline().strip()))

color = ["B", "W"]
min_change = 1000000000
# 모든 8*8 grid 후보들을 체크하기 위함
for h in range(0, (height - 8) + 1):
    for w in range(0, (width - 8) + 1):
        for color_id in range(2): # 맨 왼쪽 위가 B일 때/ W일 때를 모두 체크하기 위함
            count = 0
            current = color_id
            # 8*8 grid 안의 모든 칸을 확인한다.
            for i in range(8):
                for j in range(8):
                    if board[h+i][w+j] != color[current]: # 이상적인 값과 다르면 count한다
                        count += 1
                    if j != 7: # 줄의 마지막 글자 = 그 다음 줄의 첫 글자
                        current ^= 1

            if count < min_change:
                min_change = count

print(min_change)
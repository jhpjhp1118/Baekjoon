# https://www.acmicpc.net/problem/11650
import sys
n = int(sys.stdin.readline())

# 좌표값 input으로 받기
coords = []
for _ in range(n):
    coord = sys.stdin.readline().strip().split()
    coord = list(map(int, coord))
    coords.append(coord)

# x축에 대해 먼저 정렬한 뒤, y축에 대해 정렬하기
coords = sorted(coords, key=lambda coords : [coords[0], coords[1]])

for c in coords:
    print(c[0], c[1])

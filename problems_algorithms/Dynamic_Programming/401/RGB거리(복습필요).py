# https://www.acmicpc.net/problem/1149
import sys

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))
# 2차원 배열 생성하기 (배열크기: (n+1) by 3)
result = [[0,0,0]]

# (각 색깔 값) + (직전의 다른 색깔 비용합 중, 더 작은 값) 기록해가기
for i in range(1, n+1):
    sum_R_end = data[i-1][0] + min(result[i-1][1], result[i-1][2]) # R 로 끝나는 후보 sum 값 기록하기
    sum_G_end = data[i-1][1] + min(result[i-1][0], result[i-1][2]) # G 로 끝나는 후보 sum 값 기록하기
    sum_B_end = data[i-1][2] + min(result[i-1][0], result[i-1][1]) # B 로 끝나는 후보 sum 값 기록하기
    result.append([sum_R_end, sum_G_end, sum_B_end])

print(min(result[n]))

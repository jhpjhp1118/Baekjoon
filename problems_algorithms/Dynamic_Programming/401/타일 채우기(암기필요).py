# https://www.acmicpc.net/problem/2133
import sys

n = int(sys.stdin.readline().strip())
# 참고링크: https://ahn3330.tistory.com/81
result = [0]*31
result[0] = 1 # 점화식을 진행시키기 위해, 1로 초기화함

for i in range(2, n+1, 2): # 2, 4, ..., n까지
    # i-2칸까지의 경우의 수 * 2칸짜리 경우의 수(= 3)
    result[i] += result[i-2]*3
    for j in range(0, i-2, 2): # 0, 2, ..., i-4까지
        # 4칸을 차지하는 특수한 경우의 수, ... 4 + 2x 칸을 차지하는 특수한 경우의 수
        result[i] += result[j]*2

print(result[n])

# https://www.acmicpc.net/problem/17404
import sys

n = int(sys.stdin.readline().strip())
data = [[0, 0, 0]]
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))


ans = 1e9
for i in range(3):
    # 2차원 배열 생성하기 (배열크기: (n+1) by 3)
    result = [[1e9, 1e9, 1e9] for _ in range(n+1)] # 전부 매우 큰 값으로 초기화
    result[1][i] = data[1][i] # (핵심!)한 색깔만 초기값 기록하기 --> 해당 색깔로 시작하는 경우들 중 최소 비용을 찾게 됨

    # (각 색깔 값) + (직전의 다른 색깔 비용합 중, 더 작은 값) 기록해가기
    for j in range(2, n+1):
        sum_R_end = data[j][0] + min(result[j-1][1], result[j-1][2]) # R 로 끝나는 후보 sum 값 기록하기
        sum_G_end = data[j][1] + min(result[j-1][0], result[j-1][2]) # G 로 끝나는 후보 sum 값 기록하기
        sum_B_end = data[j][2] + min(result[j-1][0], result[j-1][1]) # B 로 끝나는 후보 sum 값 기록하기
        result[j] = [sum_R_end, sum_G_end, sum_B_end]

    # i번째 색깔로 시작하는 경우들 중, 끝 색깔이 i번째 색깔이 아닌 것만 탐색한다.
    for j in range(3):
        if i != j:
            # 더 작은 값이 나오면, 그것을 최솟값으로 기록한다.
            ans = min(ans, result[n][j])

print(ans)


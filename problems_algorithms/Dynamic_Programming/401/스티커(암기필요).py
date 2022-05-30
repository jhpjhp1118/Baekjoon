# https://www.acmicpc.net/problem/9465
# 참고링크: https://pacific-ocean.tistory.com/197
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    data = []
    for _ in range(2):
        data.append(list(map(int, sys.stdin.readline().strip().split())))

    for i in range(1, n):
        # 2번째 data 는, 대각선 방향의 1번째 data 값을 단순하게 더한다
        if i == 1:
            data[0][i] += data[1][i-1]
            data[1][i] += data[0][i-1]
        # 3번째 이후부터는, (대각선 방향의 직전 최대값) 과 (대각선 방향의 직직전 최대값) 중 더 큰 것에
        # 현재 data 값을 더한다
        else:
            data[0][i] += max(data[1][i-2], data[1][i-1])
            data[1][i] += max(data[0][i-2], data[0][i-1])

    print(max(data[0][n-1], data[1][n-1]))

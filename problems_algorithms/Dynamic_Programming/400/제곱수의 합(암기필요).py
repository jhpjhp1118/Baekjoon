# https://www.acmicpc.net/problem/1699
import sys

n = int(sys.stdin.readline().strip())

# 1만 더해서 횟수를 세면, 최대값이 된다. -> 최대값으로 가정하고 result 배열 초기화
result = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        # j의 제곱이 i보다 커지면 탐색을 끝낸다 ex) i = 8 일 때, j = 3부터는 탐색할 필요없다
        if j*j > i:
            break
        # (i - j의 제곱)에 j의 제곱을 1번 더한 횟수가, 현재 result[i]에 들어간 수보다 작으면, 그것으로 기록한다.
        if result[i] > result[i - j*j] + 1: # !! j*j 대신 j**2를 하면 시간 초과 뜸!
            result[i] = result[i - j*j] + 1

print(result[n])
# https://www.acmicpc.net/problem/10844
import sys
n = int(sys.stdin.readline().strip())
result = [[0]*10 for _ in range(101)]

#  n = 1일 때, 0~9로 끝나는 계단 수의 갯수들
result[1] = [0] + [1]*9

for i in range(2, n+1):
    # i 개의 자릿수를 가지는 계단 수의 갯수를 탐색한다.
    for j in range(10):
        # 맨 오른쪽 끝 수 = 0인건, xx...x10 밖에 없다
        if j == 0:
            result[i][j] = result[i-1][j+1]%1000000000
        # 맨 오른쪽 끝 수 = 9인건, xx...x89 밖에 없다
        elif j == 9:
            result[i][j] = result[i-1][j-1]%1000000000
        # 맨 오른쪽 끝 수 = 1~8인건, xx...x(j-1)(j) 와 xx...x(j+1)(j) 이 있다
        else:
            result[i][j] = (result[i-1][j-1] + result[i-1][j+1])%1000000000
print(sum(result[n])%1000000000)


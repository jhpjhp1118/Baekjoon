# https://www.acmicpc.net/problem/11057
import sys

n = int(sys.stdin.readline().strip())
mod = 10007

result = [[0]*10 for _ in range(n+1)]
result[1] = [1]*10

# 점화식 유도: ex) i개의 자리수를 가지고, 2로 끝나는 수 = i-1개의 자리수를 가지고, (0~2)로 끝나는 경우의 수를 모두 합한 것
# result[i][0] = result[i-1][0]
# result[i][1] = result[i-1][0]  + result[i-1][1]

for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            result[i][j] += result[i-1][k]%mod

print(sum(result[n])%mod)

# ==================================================================
# 메모리, 계산시간 적으로 더 효율적인 버전
# 저장하는 메모리: (n+1) by 10칸짜리 2차원 배열 --> 10칸짜리 1차원 배열
# i개의 자리수를 가지고, j-1로 끝나는 수 = i-1개의 자리수를 가지고, (0~j-1) 로 끝나는 경우의 수를 모두 합한 것
n = int(sys.stdin.readline().strip())

num = [1]*10

for i in range(n-1):
    for j in range(1, 10):
        num[j] += num[j-1]

print(sum(num)%10007)
# 출처: https://jainn.tistory.com/91 [Dogfootruler Kim:티스토리]
# https://www.acmicpc.net/problem/1748
import sys

n = int(sys.stdin.readline().strip())

numDigit = 0
# 1~9 --> 9*1
# 10~99 --> 90*2
# 100~999 --> 900*3
# 1 ~ (n과 동일한 자리수를 가지는 10의 거듭제곱수 - 1) 까지 이어붙였을 때의 자리수 세기
for i in range(len(str(n)) - 1):
    numDigit += 9*10**(i)*(i+1)
# (n과 동일한 자리수를 가지는 10의 거듭제곱수) ~ n 까지 이어붙였을 때의 자리수 세기
numDigit += (n - 10**(len(str(n)) - 1) + 1)*len(str(n))

print(numDigit)

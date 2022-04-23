# https://www.acmicpc.net/problem/11005
import sys

n, b = map(int, sys.stdin.readline().strip().split())
result = ""

# 10이상인 숫자는 알파벳으로 표현한다. (A:10, B:11 ~ Z:35)
alpha = [chr(ord("A") + x) for x in range(26)]

if n == 0: # n 이 0이면, 바로 0 출력한다
    print("0")
    exit()

while True:
    residual = n%b

    if residual: # 나머지가 0이 아닐 경우
        if b > 10 and residual >= 10:
            result = alpha[residual - 10] + result
        else:
            result = str(residual) + result
        if n < b: # 현재 숫자가 b보다 작을 경우, 현재 숫자까지만 출력하고, 루프를 종료한다
            break
    else: # 나머지가 0일 경우
        result = "0" + result
    n //= b

print(result)


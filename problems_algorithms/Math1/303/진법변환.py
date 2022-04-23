# https://www.acmicpc.net/problem/2745
import sys

n, b = sys.stdin.readline().strip().split()
b = int(b)
result = 0

# 10이상인 숫자는 알파벳으로 표현한다. (A:10, B:11 ~ Z:35)
alpha = [chr(ord("A") + x) for x in range(26)]

# alpha를 딕셔너리로 전환한다.
alpha_dict = {}
for i, ch in enumerate(alpha):
    alpha_dict[ch] = i + 10

power = len(n) - 1 # n의 맨 앞자리 수의 지수
# 한글자씩 탐색하면서, 숫자를 더해간다.
for char in n:
    if char.isalpha(): # char이 알파벳일 경우, 딕셔너리를 참고해서 값을 더한다.
        result += alpha_dict[char]*b**power
    else: # char이 숫자일 경우, (숫자*b^power) 를 더한다.
        result += int(char)*b**power
    power -= 1
print(result)

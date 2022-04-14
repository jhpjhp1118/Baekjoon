# https://www.acmicpc.net/problem/1935
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()

# 딕셔너리에 문자별 숫자 기록해놓기
dictNum = {}
ascii = ord("A")
for _ in range(n):
    ch = int(sys.stdin.readline().strip())
    dictNum[chr(ascii)] = ch
    ascii += 1

stack = deque()
for char in line:
    if char.isalpha(): # char이 알파벳(사실상 숫자)일 때
        stack.append(dictNum[char])
    else: # char이 수식기호일 때
        b = stack.pop()
        a = stack.pop()
        if char == "+":
            stack.append(a + b)
        elif char == "-":
            stack.append(a - b)
        elif char == "*":
            stack.append(a * b)
        elif char == "/":
            stack.append(a / b)
print("{:.2f}".format(round(stack[0], 2)))

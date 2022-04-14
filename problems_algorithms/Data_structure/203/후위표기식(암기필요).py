# https://www.acmicpc.net/problem/1918
import sys
from collections import deque

line = sys.stdin.readline().strip()

stack = deque()
result = ""
for char in line:
    if char.isalpha():
        result += char
    else:
        if char == "(":
            stack.append(char)
        elif char == "*" or char == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(char)
        elif char == "+" or char == "-":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop() # 스택 끝에 남아있는 "(" 없애기 (후위 표기식은 괄호가 안 쓰인다)

while stack: # 마지막에 남은 기호들 다 털어내기
    result += stack.pop()
print(result)

# stack: 기호를 넣는 자료구조
# 알파벳 --> 볼때마다 출력
# ( --> ) 나올때까지 모든 기호 append했다가, ) 나오면 ( 나올때까지 pop 출력
# *, / -->
# +, - -->
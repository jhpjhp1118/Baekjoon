# https://www.acmicpc.net/problem/17413
import sys
from collections import deque

stack = deque()
flag = 0 # "<"가 나왔으면 1, 태그가 끝났으면 0
line = sys.stdin.readline().strip()
line += " "
for i, char in enumerate(line):
    if char == "<":
        # 그 전까지 담아놓은 것들을 전부 거꾸로 출력한다.
        while stack and (flag == 0):
            print(stack.pop(), end="")
        # <가 나왔음을 표시해놓고, >가 나올 때까지 append한 뒤, popleft 한다
        flag = 1
        stack.append(char)
    elif char == ">":
        stack.append(char)
        while stack:
            print(stack.popleft(), end="")
        flag = 0
    elif char == " ":
        if flag == 0:
            while stack:
                print(stack.pop(), end="")
            if i != len(line) - 1:
                print(" ", end="")
        else:
            stack.append(char)
    else:
        stack.append(char)



# stack에 append한 것이 < 일때: >가 append될 때까지 append하고, >가 나오면 popleft() 한다

# stack에 append하다가, [<," "] 가 나왔을 때 pop() 한다.

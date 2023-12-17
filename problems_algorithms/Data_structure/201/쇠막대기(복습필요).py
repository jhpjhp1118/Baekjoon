# https://www.acmicpc.net/problem/10799
import sys
from collections import deque

line = sys.stdin.readline().strip()
stack = deque()
flag = 0 # ")"가 직전에 나왔으면 1, "("가 나왔으면 0
count = 0
for char in line:
    if char == ")":
        if flag == 0: # 레이저
            stack.pop() # 레이저 기호 "(" 제거하기
            count += len(stack)
            flag = 1
        else: # stack의 제일 위쪽 막대기의 끝
            stack.pop() # 제일 위쪽 막대기의 시작점 제거하기
            count += 1
    else:
        stack.append(char)
        flag = 0
print(count)




#
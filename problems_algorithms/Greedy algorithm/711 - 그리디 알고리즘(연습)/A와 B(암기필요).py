# https://www.acmicpc.net/problem/12904
import sys

input = sys.stdin.readline

"""
아이디어: 더 긴 문자열인 T에서 S로 바뀌는 상황으로 해석한다.
    현재 T의 마지막 글자가 무엇인지에 따라
    A) 뒤에서 A를 제거한다.
    B) 뒤에서 B를 제거하고, 순서를 뒤집는다.
    T가 S와 같을 길이가 될 때까지, 위의 2가지 action을 취한 뒤, 비교한다. 
"""

s = list(input().strip())
t = list(input().strip())

sLen = len(s) # s 길이

# t의 길이가 s와 같아질 때까지 반복한다.
while len(t) > sLen:
    # t의 마지막 글자가 A이면, 뒤에서 A를 제거한다.
    if t[-1] == "A":
        t.pop()
    # t의 마지막 글자가 B이면, 뒤에서 B를 제거하고, 순서를 뒤집는다.
    elif t[-1] == "B":
        t.pop()
        t.reverse()

# t의 길이가 s와 같아졌을 때, 둘이 동일한지 비교해서 결과를 출력한다.
if t == s:
    print(1)
else:
    print(0)

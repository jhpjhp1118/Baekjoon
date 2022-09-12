# https://www.acmicpc.net/problem/12904
import sys
from collections import deque

input = sys.stdin.readline

"""
아이디어: 더 긴 문자열인 T에서 S로 바뀌는 상황으로 해석한다.
    
    A) 현재 T의 마지막 글자가 A이면,
        뒤에서 A를 제거한다.
    
    B) 현재 T의 첫 글자가 B이면,
        순서를 뒤집고, B를 제거한다.
    T가 S와 같을 길이가 될 때까지, 위의 2가지 action을 취하는 것을 bfs로 탐색해서, 비교한다. 
"""

s = list(input().strip())
t = list(input().strip())

def bfs(s, t):
    q = deque()
    q.append(t)
    sLen = len(s)  # s 길이

    while q:
        tNow = q.popleft()
        # tNow와 s의 길이가 같아지면, tNow가 s와 같은지 비교한다.
        if len(tNow) == sLen:
            # 같으면 True 를 반환하고, 아니면 skip 한다.
            if tNow == s:
                return True
            else:
                continue
        # tNow의 마지막 글자가 A 이면, 다음 탐색 대상으로 A를 제거한 것을 추가한다.
        if tNow[-1] == "A":
            q.append(tNow[:-1])
        # tNow의 첫 글자가 B 이면, 다음 탐색 대상으로 순서를 뒤집고, B를 제거한 것을 추가한다.
        if tNow[0] == "B":
            q.append(tNow[::-1][:-1])

    return False

# bfs로 탐색해서 결과에 따라 출력한다.
if bfs(s, t):
    print(1)
else:
    print(0)

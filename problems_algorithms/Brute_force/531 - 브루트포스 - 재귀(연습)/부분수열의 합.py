# https://www.acmicpc.net/problem/14225
import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

"""
아이디어: 1182번 "부분수열의 합"이랑 기본은 똑같음. 마지막 답을 찾는 부분만 다름
"""
# 출력 가능한 숫자를 비트마스크로 저장할 리스트
possible = [0] * int(2*1e6) 

def dfs(bit, idx):
    if idx == n:
        val = sum([bit[i] * nums[i] for i in range(n)])
        # 출력가능한 숫자라는 뜻으로 1을 기록한다.
        possible[val - 1] = 1 # 인덱스를 맞추기 위해 1을 뺀다.
        return

    for i in range(2):
        bit[idx] = i
        dfs(bit=bit, idx=idx + 1)

dfs(bit=[0]*n, idx=0)
print(possible.index(0) + 1) # 인덱스 맞추기 때문에 1을 더한다.


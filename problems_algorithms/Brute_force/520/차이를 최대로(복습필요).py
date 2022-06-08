# https://www.acmicpc.net/problem/10819
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

s = []
global ans
ans = 0

def dfs():
    global ans
    if len(s) == n:
        # 차이 절대값들의 합을 구한 뒤, 최대값이면 갱신한다.
        diffSum = sum([abs(arr[s[i]] - arr[s[i+1]]) for i in range(n-1)])
        if diffSum > ans:
            ans = diffSum
        return

    for i in range(n):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
print(ans)


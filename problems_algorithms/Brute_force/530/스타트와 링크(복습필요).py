# https://www.acmicpc.net/problem/14889
import sys
# 핵심 아이디어: 스타트가 0(문제에선 1. 아무튼 첫번째 사람)을 포함하는 팀들만 탐색하면, 다른 경우는 더 탐색할 필요 없다!
# 이유: 예를 들어, n = 6일 경우, 1을 포함하는 팀의 갯수: 5C2 개
#                             각각의 반대팀의 갯수: 5C3 개 --> 둘은 동일하다.

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

global ans
ans = int(1e9)

def dfs(s):
    global ans

    if len(s) == n//2 - 1:
        # 스타트 팀의 능력치를 계산한다
        cost1 = 0
        for i in range(len(s)):
            cost1 += data[0][s[i]] + data[s[i]][0]
            for j in range(i+1, len(s)):
                cost1 += data[s[i]][s[j]] + data[s[j]][s[i]]
        # 링크 팀의 능력치를 계산한다.
        l = [i for i in range(1, n) if i not in s]
        cost2 = 0
        for i in range(len(s)+1):
            for j in range(i + 1, len(s)+1):
                cost2 += data[l[i]][l[j]] + data[l[j]][l[i]]
        # 최소값이면 갱신한다.
        ans = min(ans, abs(cost1 - cost2))
        return

    # 스타트 팀이 0을 포함하는 경우에 대해서만 탐색을 진행한다.
    for i in range(1, n):
        if i not in s and (len(s) == 0 or s[-1] < i):
            s.append(i)
            dfs(s)
            s.pop()

dfs(s=[])
print(ans)

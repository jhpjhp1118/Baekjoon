# https://www.acmicpc.net/problem/14889
import sys

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

global ans
ans = int(1e9)

def dfs(s):
    global ans

    if len(s) == n//2 - 1:

        cost1 = 0
        for i in range(len(s)):
            cost1 += data[0][s[i]] + data[s[i]][0]
            for j in range(i+1, len(s)):
                cost1 += data[s[i]][s[j]] + data[s[j]][s[i]]

        l = [i for i in range(1, n) if i not in s]
        # print(s, l)
        cost2 = 0
        for i in range(len(s)+1):
            for j in range(i + 1, len(s)+1):
                cost2 += data[l[i]][l[j]] + data[l[j]][l[i]]

        ans = min(ans, abs(cost1 - cost2))


    for i in range(1, n):
        if i not in s and (len(s) == 0 or s[-1] < i):
            s.append(i)
            dfs(s)
            s.pop()

dfs(s=[])
print(ans)

# https://www.acmicpc.net/problem/11052
import sys

n = int(sys.stdin.readline().strip())
ps = list(map(int, sys.stdin.readline().strip().split()))
ps.insert(0, 0)

result = [ps[0], ps[1]] # n=0, 1일 때의 결과값들


for i in range(2, n + 1):
    compare = []
    for j in range(i): # j = 0 ~ i-1 까지 탐색
        compare.append(result[j] + ps[i-j]) # ex) n = 2--> i = 2 --> j = 0 1, i-j = 2 1
    result.append(max(compare)) # 후보들 중, 최대값을 결과에 추가한다
print(result[n])


# https://www.acmicpc.net/problem/16194
import sys

n = int(sys.stdin.readline().strip())
ps = list(map(int, sys.stdin.readline().strip().split()))
ps.insert(0, 0) # 0개의 카드의 값은 0이라고 가정한다. (사실상 안쓰는 데이터. 인덱스 처리용)

result = [ps[0], ps[1]] # n=0, 1일 때의 최소 비용들


for i in range(2, n + 1):
    compare = []
    # i 장을 사는 상황에서, j장을 사는 최소 비용 + (i-j)장을 사는 비용을 전부 탐색 --> 그 중 최소값을 찾는다.
    for j in range(i): # j = 0 ~ i-1 까지 탐색
        compare.append(result[j] + ps[i-j]) # ex) n = 2--> i = 2 --> j = 0 1, i-j = 2 1
    result.append(min(compare)) # 후보들 중, 최소값을 결과에 추가한다
print(result[n])




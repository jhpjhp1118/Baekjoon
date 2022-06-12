# https://www.acmicpc.net/problem/15661
import sys
# 핵심 아이디어: 스타트가 0(문제에선 1. 아무튼 첫번째 사람)을 포함하고, 인원수가 2 ~ n-2인 팀들만 탐색하면, 다른 경우는 더 탐색할 필요 없다!
# 이유: 예를 들어, n = 6일 경우, 1을 포함하는 팀의 갯수: 5C2 개
#                             각각의 반대팀의 갯수: 5C3 개 --> 둘은 동일하다.
# 인원수가 1 & n-1인 경우는, 1명인 팀의 능력치 합이 0이므로, 의미없는 경우이다.

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

global ans
ans = int(1e9)

def dfs(s, l, cost1, cost2):
    global ans
    # 최소 차이 값을 갱신해준다.
    ans = min(ans, abs(cost1 - cost2))

    # 스타트 팀의 인원 수가 n-2 가 될 때까지만 탐색한다. (스타트 팀이 1명 or n-1명인 경우는, 1명인 팀의 능력치 합이 0이므로 의미없다.)
    if len(s) == n - 2:
        return

    # 스타트 팀이 0을 포함하는 경우에 대해서만 탐색을 진행한다.
    for i in range(1, n):
        if i not in s and s[-1] < i:
            # i가 스타트팀에 추가됨으로써 늘어나는 cost1 값을 계산한다.
            val1 = 0
            for j in s:
                val1 += data[i][j] + data[j][i]
            # i가 링크팀에서 제외됨으로써 줄어드는 cost2 값을 계산한다.
            val2 = 0
            for j in l:
                val2 += data[i][j] + data[j][i]
            # i를 스타트팀에 추가, 링크팀에서는 제외
            s.append(i)
            l.remove(i)
            # 한 단계 더 깊이 탐색을 들어간다.
            dfs(s, l, cost1=cost1 + val1, cost2=cost2 - val2)
            # i를 스타트팀에서는 제외, 링크팀에 추가
            s.pop()
            l.append(i)
            # 링크팀의 마지막 성분으로 i를 추가해줬으므로, 정렬을 계속 해준다.
            l = sorted(l)
# 일단 첫번째 멤버만 없는 것으로 링크팀 구성하기
l = [i for i in range(1, n)]
# 링크 팀의 능력치 합 구해주기
cost2 = 0
for i in range(1, n):
    for j in range(i, n):
        cost2 += data[i][j] + data[j][i]

dfs(s=[0], l=l, cost1=0, cost2=cost2)

print(ans)


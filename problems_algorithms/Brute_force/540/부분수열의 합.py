# https://www.acmicpc.net/problem/1182
import sys

n, s = list(map(int, sys.stdin.readline().strip().split()))
arr = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0
def dfs(bit, idx):
    global cnt

    # 직전의 idx 가 0이었고 그 다음으로 dfs를 들어온 것이라면, 거기서 탐색을 종료하고, 성분 합을 확인해본다.
    if idx == -1:
        sumVal = sum([bit[i] * arr[i] for i in range(n)])
        # bit의 모든 값이 0인 경우는 제외하고, 성분값을 확인한다.
        if sum(bit) != 0 and sumVal == s:
            cnt += 1
        return
    # bit리스트의 idx번째 자리에 0, 1 을 순차적으로 넣어보며 탐색한다.
    for i in range(2):
        bit[idx] = i
        dfs(bit, idx - 1)

dfs(bit=[0]*n,idx=n-1)
print(cnt)



# https://www.acmicpc.net/problem/6603
import sys

def dfs(s):
    if len(s) == 6:
        print(*s)
        return
    
    # 가지치기
    # s에 성분이 하나라도 있을 때, 만약 data 안에서, 
    # s의 마지막 성분보다 큰 값의 갯수 < 6개까지 더 뽑아야 하는 성분의 갯수 이면,
    # 탐색을 종료한다.
    if len(s) != 0 and k - 1 - data.index(s[-1]) < 6 - len(s):
        return

    for val in data:
        if val not in s and (len(s) == 0 or s[-1] < val):
            s.append(val)
            dfs(s)
            s.pop()


while True:
    arr = list(map(int, sys.stdin.readline().strip().split()))
    if arr[0] == 0:
        break

    k = arr[0]
    data = arr[1:]

    dfs(s=[])
    print()


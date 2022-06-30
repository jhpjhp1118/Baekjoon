# https://www.acmicpc.net/problem/16929
import sys
# 참고링크: https://data-flower.tistory.com/100
# 핵심 아이디어: dfs의 깊이가 4 이상이고, 처음 위치가 현재의 탐색 후보군에 있으면, 사이클이다!

n, m = list(map(int, sys.stdin.readline().strip().split()))

data = []
for _ in range(n):
    data.append(list(sys.stdin.readline().strip()))

steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]


global flag
flag = False

# 함수 정의하기
def dfs(char, row, col, cnt, rStart, cStart):
    global flag
    # 만약 사이클이 발견되었으면, 탐색을 종료한다.
    if flag:
        return

    for k in range(4):
        r, c = row + steps[k][0], col + steps[k][1]
        # 좌표 범위를 벗어나는 경우, skip 한다.
        if r < 0 or r >= n or c < 0 or c >= m:
            continue

        # 깊이가 4 이상이고, 처음 칸이면, 사이클로 간주하고 탐색을 종료한다.
        if cnt >= 4 and r == rStart and c == cStart:
            flag = True
            return
        # 같은 문자이고, 방문하지 않은 칸이면, 탐색을 더 깊게 진행한다.
        if data[r][c] == char and not visited[r][c]:
            visited[r][c] = True
            dfs(char, r, c, cnt=cnt + 1, rStart=rStart, cStart=cStart)
            visited[r][c] = False


visited = [[False]*m for _ in range(n)]

# 한 칸마다, dfs 함수를 적용시켜보기
for i in range(n):
    for j in range(m):
        visited[i][j] = True

        dfs(char=data[i][j], row=i, col=j, cnt=1, rStart=i, cStart=j)

        # 만약 사이클이 있다면, Yes를 출력하고 바로 프로그램 종료하기
        if flag:
            print("Yes")
            exit()
# 만약 사이클이 없다면, No를 출력하기
print("No")
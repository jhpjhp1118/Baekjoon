import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    # 가지치기용. 지금까지의 값 + 남은 횟수만큼 arr의 최대값을 더해도 갱신이 안될 경우, 해당 가지를 skip 한다
    if ans >= total + max_val * (3 - idx):
        return

    # 4번째 칸을 방문했을 경우, 최대값을 갱신한다.
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        # step별로 탐색한다.
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                # 뻐큐 모양 블록
                if idx == 1:
                    # 3번째 칸을 방문은 하지만, 다시 2번째 칸에서 탐색을 한다 --> 뻐큐 모양을 의미함
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr)) # arr의 최대값 성분

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
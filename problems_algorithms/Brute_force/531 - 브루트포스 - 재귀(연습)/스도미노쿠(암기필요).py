# https://www.acmicpc.net/problem/4574
# 참고링크: https://derooty.tistory.com/53

"""
설명
행렬 R: 각 row에 1~9 의 값이 현재 채워져 있는지를 나타낸 행렬 (있으면 1, 없으면 0)
행렬 C: 각 col에 1~9 의 값이 현재 채워져 있는지를 나타낸 행렬 (있으면 1, 없으면 0)
행렬 S: 각 square에 1~9 의 값이 현재 채워져 있는지를 나타낸 행렬 (있으면 1, 없으면 0)

<3*3 크기의 square가 9*9 grid에서 나열된 번호 순서>
1 2 3
4 5 6
7 8 9
"""

import sys
input = sys.stdin.readline

def go(cnt, itr):
    find = False

    # cnt == 총 빈칸의 갯수일 경우 (cnt = 0 에서부터 시작했으므로), 완성된 스도쿠를 출력하고, 탐색을 종료한다.
    if cnt == Ecnt:
        print('Puzzle', itr)
        for r in range(9):
            for c in range(9):
                print(A[r][c], end='')
            print()
        return True

    # 빈 칸 1개를 E 리스트에서 받아온다.
    r, c = E[cnt]

    # 만약 현재 탐색 대상인 위치에 대해, 빈 칸이 아닐 경우, 다음 빈 칸으로 넘어간다.
    if A[r][c]:
        find = go(cnt + 1, itr)
        return find

    for i in range(9):
        for j in range(9):
            # Visit 행렬의 대각 성분일 경우 or 이미 방문한 도미노일 경우, skip한다.
            if i == j or Visit[i][j]:
                continue

            for d in dr: # 탐색의 중심의 되는 칸에서부터, 1) 오른쪽 칸 2) 아래쪽 칸 으로 탐색해본다.
                pair_x, pair_y = r + d[0], c + d[1]
                # 탐색하고 있는 칸의 위치가 grid 범위를 벗어나지 않고, 스도쿠상으로 빈 칸일 경우
                if 0 <= pair_x <= 8 and 0 <= pair_y <= 8 and not A[pair_x][pair_y]:
                    # 탐색의 중심 칸 & 탐색하고 있는 칸이 속한 row, col, square 에서 전부 중복되지 않는 값일 경우
                    if R[r][i] == R[pair_x][j] == C[c][i] == C[pair_y][j] == S[r // 3 * 3 + c // 3][i] == S[pair_x // 3 * 3 + pair_y // 3][j] == 0:
                        A[r][c], A[pair_x][pair_y] = i + 1, j + 1 # 스도쿠 grid의 각 칸에 값을 채워넣는다.
                        Visit[i][j], Visit[j][i] = 1, 1 # 도미노 방문 여부를 1로 작성한다. (방문했다는 뜻)
                        # 각 row, col, square에 대해, 해당 값을 채웠다고 기록한다.
                        R[r][i], R[pair_x][j], C[c][i], C[pair_y][j], S[r // 3 * 3 + c // 3][i], S[
                            pair_x // 3 * 3 + pair_y // 3][j] = 1, 1, 1, 1, 1, 1
                        # 다음 빈 칸으로 탐색을 진행한다.
                        find = go(cnt + 1, itr)
                        # 더 깊은 탐색이 성공적이었을 경우, True 를 리턴한다.
                        if find:
                            return find

                        # 채워넣었던 스도쿠 grid 및 기록들을 되돌린다.
                        A[r][c], A[pair_x][pair_y] = 0, 0
                        Visit[i][j], Visit[j][i] = 0, 0
                        R[r][i], R[pair_x][j], C[c][i], C[pair_y][j], S[r // 3 * 3 + c // 3][i], S[
                            pair_x // 3 * 3 + pair_y // 3][j] = 0, 0, 0, 0, 0, 0
    return find


itr = 1 # puzzle 번호
while True:
    N = int(input()) # 도미노 갯수 입력받기
    dr = [[0, 1], [1, 0]] # 1) 오른쪽 1칸 전진 2) 아래쪽 1칸 전진

    # 마지막 줄인 경우 (N = 0), 프로그램을 종료한다.
    if N == 0:
        break
    A = [[0] * 9 for _ in range(9)]
    Visit = [[0] * 9 for _ in range(9)] # 방문했으면 해당 자리에 1, 방문안했으면 0으로 채워놓는 grid
    R = [[0] * 9 for _ in range(9)]
    C = [[0] * 9 for _ in range(9)]
    S = [[0] * 9 for _ in range(9)]
    E = [] # 빈 칸의 좌표를 저장할 리스트
    Ecnt = 0 # 빈 칸의 갯수
    for _ in range(N):
        U, LU, V, LV = input().split() # 도미노 1개의 정보 입력받기
        U_x, U_y = ord(LU[0]) - ord('A'), int(LU[1]) - 1 # 도미노의 첫번째 숫자 위치
        V_x, V_y = ord(LV[0]) - ord('A'), int(LV[1]) - 1 # 도미노의 두번째 숫자 위치
        A[U_x][U_y], A[V_x][V_y] = int(U), int(V) # 스도쿠 자리에, 도미노의 값들 채워넣기
        Visit[int(U) - 1][int(V) - 1], Visit[int(V) - 1][int(U) - 1] = 1, 1 # 해당 값의 조합에 대해, 방문 여부를 1로 표시하기
        R[U_x][int(U) - 1], R[V_x][int(V) - 1] = 1, 1 # 해당 row의 해당 값에 대해, 방문 여부를 1로 표시하기
        C[U_y][int(U) - 1], C[V_y][int(V) - 1] = 1, 1 # 해당 col의 해당 값에 대해, 방문 여부를 1로 표시하기
        S[U_x // 3 * 3 + U_y // 3][int(U) - 1] = 1 # 세로좌표: ???, 가로좌표: 값
        S[V_x // 3 * 3 + V_y // 3][int(V) - 1] = 1

    for i, pos in enumerate(input().split()): # 9개의 single 값들 입력받기
        pos_x, pos_y = ord(pos[0]) - ord('A'), int(pos[1]) - 1 # 각 single 값의 위치
        A[pos_x][pos_y] = i + 1 # 스도쿠 값 채워넣기
        R[pos_x][i], C[pos_y][i] = 1, 1 # 해당 row, col & 해당 값에 대해, 방문 여부 1로 표시하기
        S[pos_x // 3 * 3 + pos_y // 3][i] = 1 # 세로좌표: ???, 가로좌표: 값
    for r in range(9):
        for c in range(9):
            if not A[r][c]: # 스도쿠 grid에서, 값이 아직 0인(아직 채워지지 않은) 자리에 대해,
                E.append([r, c]) # 빈 칸을 E 리스트에 append한다
                Ecnt += 1 # 빈 칸의 갯수를 count 한다.
    go(0, itr)
    itr += 1 # 현재 puzzle을 풀고 나면, 다음 puzzle로 넘어간다.



# https://www.acmicpc.net/problem/3085
import sys

# 함수 역할: 주어진 data table에 대해, 최대 연속 문자의 갯수(ans)를 찾아낸다.
def check(data):
    n = len(data)
    ans = 1

    # 왼쪽 위 --> 오른쪽 아래 대각선 방향으로 탐색한다.
    for i in range(n):

        # 가로 방향으로 탐색
        cnt = 1
        for j in range(1, n):
            if data[i][j-1] == data[i][j]:
                cnt += 1
            else:
                cnt = 1
            # 현재 ans 값보다 더 큰 cnt가 나오면, 그 cnt로 ans를 대체한다.
            if cnt > ans:
                ans = cnt

        # 세로 방향으로 탐색
        cnt = 1
        for j in range(1, n):
            if data[j-1][i] == data[j][i]:
                cnt += 1
            else:
                cnt = 1
            # 현재 ans 값보다 더 큰 cnt가 나오면, 그 cnt로 ans를 대체한다.
            if cnt > ans:
                ans = cnt

    return ans

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
    data.append(list(sys.stdin.readline().strip()))

# 모든 가능한 칸에 대해, 오른쪽 or 아래쪽으로 성분을 바꿔가면서 check 함수 값을 확인한다 --> 최대값을 출력한다.
ans = 1
for i in range(n):
    for j in range(n):
        # i번째 행이 마지막 행이 아닐 경우, 1칸을 아래쪽으로 성분 교체하여 check 함수 값을 확인한 뒤, 다시 복원한다.
        if i < n - 1:
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
            num = check(data)
            if num > ans:
                ans = num
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
        # j번째 행이 마지막 열이 아닐 경우, 1칸을 오른쪽으로 성분 교체하여 check 함수 값을 확인한 뒤, 다시 복원한다.
        if j < n - 1:
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            num = check(data)
            if num > ans:
                ans = num
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]

print(ans)

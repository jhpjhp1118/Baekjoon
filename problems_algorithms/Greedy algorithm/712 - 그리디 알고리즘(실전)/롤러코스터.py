# https://www.acmicpc.net/problem/2873
import sys

input = sys.stdin.readline

"""
아이디어: grid의 가로, 세로 길이 중 하나라도 홀수가 있는 경우 / 전부 짝수인 경우로 나눠서 생각한다.
    1) 하나라도 홀수가 있는 경우
        모든 성분을 다 지나갈 수 있다. (ㄹ 모양으로)
        경로: 홀수인 축의 수직 방향으로 ㄹ 모양을 그리면서 순회하면 된다.
    2) 둘 다 짝수인 경우
        가장 오른쪽 아래 칸에 인접한 성분 2개 중 하나만 못 지나간다.
        둘 중 더 값이 큰 칸을 지나는 경로를 찾는다
        경로: 
            * 가장 오른쪽 아래 칸의 왼쪽 칸을 지나는 경우
                ** 세로 길이가 2보다 큰 경우
                    오른쪽으로 ㄹ 모양으로 가다가, 2 행만 남았을 때, 아래쪽으로 ㄹ모양으로 2칸 간격으로 진행한다.
                ** 세로 길이가 2보다 작은 경우,
                    바로 아래쪽으로 ㄹ 모양으로 2칸 간격으로 진행한다.
            * 가장 오른쪽 아래 칸의 위쪽 칸을 지나는 경우
                (위의 반대 버전으로 하면 된다.)
"""

r, c = list(map(int, input().strip().split()))

grid = []
for _ in range(r):
    grid.append(list(map(int, input().strip().split())))

# 방향에 맞는 문자를 반환하는 함수
def dirToChar(dir):
    if dir == (1, 0):
        return "D"
    elif dir == (-1, 0):
        return "U"
    elif dir == (0, 1):
        return "R"
    elif dir == (0, -1):
        return "L"

# ㄹ 모양으로 움직이는 경로를 생성하는 함수
def snakeMove(grid, start, end, startDir, amplitude):
    
    pos = start[:]
    path = []

    dir = startDir
    uTurnDir = (startDir[0] ^ 1, startDir[1] ^ 1)
    while True:
        # 설정한 진폭만큼 전진한다.
        pos = (pos[0] + (amplitude - 1) * dir[0], pos[1] + (amplitude - 1) * dir[1])
        path += [dirToChar(dir)] * (amplitude - 1)
        if pos == end:
            break
        
        # 유턴하기 위해 수직으로 꺾어서 1칸 움직인다.
        pos = (pos[0] + uTurnDir[0], pos[1] + uTurnDir[1])
        path += [dirToChar((uTurnDir[0], uTurnDir[1]))]
        if pos == end:
            break
        
        # 진행방향을 반대로 뒤집는다.
        dir = (-dir[0], -dir[1])

    return path


ans = []
if r % 2 == 0 and c % 2 == 0:
    # 가장 오른쪽 칸의 왼쪽 칸의 값 >= 위쪽 칸의 값인 경우
    if grid[r - 1][c - 2] >= grid[r - 2][c - 1]:
        # row가 2개만 남을 때까지, 오른쪽으로 ㄹ 모양으로 경로를 진행한다. 그리고, 아래쪽으로 1칸 전진한다.
        if r > 2:
            ans += snakeMove(grid, (0, 0), (r - 2, 0), (0, 1), c)
        # 아래쪽으로 ㄹ 모양으로 2칸 간격으로 진행한다.
        ans += snakeMove(grid, (r - 2, 0), (r - 1, c - 1), (1, 0), 2)

    # 가장 오른쪽 칸의 왼쪽 칸의 값 < 위쪽 칸의 값인 경우
    else:
        # column이 2개만 남을 때까지, 아래쪽으로 ㄹ 모양으로 경로를 진행한다. 그리고, 오른쪽으로 1칸 전진한다.
        if c > 2:
            ans += snakeMove(grid, (0, 0), (0, c - 2), (1, 0), r)
        # 오른쪽으로 ㄹ 모양으로 2칸 간격으로 진행한다.
        ans += snakeMove(grid, (0, c - 2), (r - 1, c - 1), (0, 1), 2)

# r, c 중 하나라도 홀수인 경우
else:
    # r 이 홀수인 경우
    if r % 2 == 1:
        # 오른쪽으로 ㄹ 모양을 시작하는 경로를 찾는다.
        ans += snakeMove(grid, (0, 0), (r - 1, c - 1), (0, 1), c)
    # c 가 홀수인 경우
    else:
        # 아래쪽으로 ㄹ 모양을 시작하는 경로를 찾는다.
        ans += snakeMove(grid, (0, 0), (r - 1, c - 1), (1, 0), r)

print("".join(ans))


"""
INPUT:
4 4
5 1 5 5
5 5 5 5
5 5 5 5
5 5 5 5

ANS:
DRRURDDLLLDRRR
"""


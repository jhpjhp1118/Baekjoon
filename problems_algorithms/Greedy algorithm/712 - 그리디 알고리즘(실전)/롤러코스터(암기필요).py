# https://www.acmicpc.net/problem/2873
import sys

input = sys.stdin.readline

"""
아이디어: grid의 가로, 세로 길이 중 하나라도 홀수가 있는 경우 / 전부 짝수인 경우로 나눠서 생각한다.
    1) 하나라도 홀수가 있는 경우
        모든 성분을 다 지나갈 수 있다. (ㄹ 모양으로)
        경로: 홀수인 축의 수직 방향으로 ㄹ 모양을 그리면서 순회하면 된다.
    2) 둘 다 짝수인 경우
        i,j = 홀수인 칸들 중(마치 체스판) 하나만 못 지나간다.
        이들 중 가장 값이 작은 칸을 안 지나는 경로를 찾는다
        
    참고링크) https://suri78.tistory.com/148
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
    uTurnDir = (abs(startDir[0]) ^ 1, abs(startDir[1]) ^ 1)
    while True:
        # 설정한 진폭만큼 전진한다.
        pos = (pos[0] + (amplitude - 1) * dir[0], pos[1] + (amplitude - 1) * dir[1])
        # 피해야 하는 칸이면,
        if grid[pos[0]][pos[1]] < 0:
            # 유턴하기 위해 수직으로 꺽은 방향으로 1칸 움직여서 피한다.
            pos = (pos[0] + uTurnDir[0], pos[1] + uTurnDir[1])
            # 피하는데 추가로 필요한 경로를 추가한다.
            path += [dirToChar((uTurnDir[0], uTurnDir[1]))]

        # 진폭만큼 전진한 경로를 추가한다.
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
    # i + j 가 홀수인 칸들 중에서, 가장 값이 작은 칸을 찾는다.
    minVal = 100000
    minR, minC = -1, -1
    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 1 and minVal > grid[i][j]:
                minR, minC = i, j
                minVal = grid[i][j]
    # 그 칸의 값을 음수로 만든다.
    grid[minR][minC] *= -1

    # 그 칸이 속한 2개의 row를 선별한다.
    avoidRow = minR // 2 * 2 # 해당 칸이 속한 2개의 row 중, 위에 있는 row의 번호

    # avoidRow가 2 이상이면,
    if avoidRow >= 2:
        # avoidRow 전까지, 오른쪽으로 ㄹ 모양을 시작하는 경로로 전진한다.
        ans += snakeMove(grid, (0, 0), (avoidRow - 1, 0), (0, 1), c)
        # 한 칸 아래로 내려간다.
        ans += ["D"]

    # 그 2개의 row의 가장 왼쪽 위 칸 기준으로, 아래방향으로 시작하는 ㄹ 모양 경로로 전진한다.
    # (못가는 칸은 오른쪽으로 피해간다.)
    ans += snakeMove(grid, (avoidRow, 0), (avoidRow + 1, c - 1), (1, 0), 2)

    # avoidRow가 r - 2 이 아니면,
    if avoidRow != r - 2:
        # 한 칸 아래로 내려간다.
        ans += ["D"]
        # 가장 오른쪽 아래 칸까지, 왼쪽으로 ㄹ 모양을 시작하는 경로로 전진한다.
        ans += snakeMove(grid, (avoidRow + 2, c - 1), (r - 1, c - 1), (0, -1), c)

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


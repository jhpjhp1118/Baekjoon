# https://www.acmicpc.net/problem/9663
import sys

n = int(sys.stdin.readline().strip())

"""
아이디어: 각 row 마다 서로 겹치지 않게 1개의 퀸을 놔야 한다. 각 row 마다 가능한 곳들을 두다 보면, 빠짐없이 중복되지 않게 탐색할 수 있을 것이다.
주의) 시간초과를 주의해야 함! python3는 어쩔 수 없이 시간초과 뜨는듯. PyPy3 로 설정해서 풀자.
참고 링크: https://seongonion.tistory.com/103
"""

row = [0] * n

global ans
ans = 0


def isOk(x):
    # x번째 row의 퀸이, i번째 row의 퀸과 비교했을 때,
    for i in range(x):
        # 대각선에 있을 경우, False를 리턴한다.
        if abs(row[x] - row[i]) == abs(x - i):
                return False

    return True

colUsed = [False] * n

def dfs(x):
    global ans
    # 0 ~ n-1 번째 row 까지 다 퀸을 놓았을 경우, 경우의 수를 +1 한다.
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # 아직 사용하지 않은 column이라면,
            if not colUsed[i]:
                row[x] = i
                # 해당 위치에 퀸을 놓는 것이 타당하다면, 다음 row로 탐색한다.
                if isOk(x):
                    colUsed[i] = True
                    dfs(x + 1)
                    colUsed[i] = False
dfs(0)
print(ans)


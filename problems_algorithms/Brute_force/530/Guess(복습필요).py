# https://www.acmicpc.net/problem/1248
import sys

n = int(sys.stdin.readline().strip())
arr = list(sys.stdin.readline().strip())

# 부호 행마다 쪼개기
signs = []
last = 0
for i in range(n, 0, -1):
    row = []
    for j in range(i):
        row.append(arr[last + j])
    signs.append(row)
    last += i

def check(s, row, firstElem):
    """
    해당 row의 나머지 부호들도 만족하는지 확인 (만족하지 못하면, 바로 loop를 종료하고 flag = False가 된다)
    :param s: stack
    :param row: signs에서 몇번째 row를 검증하고 있는지에 대한 변수
    :param firstElem: 해당 row에서 첫번째 성분으로 추가하려고 하는 값
    :return: 모든 부호를 만족하는지 여부
    """
    sumVal = firstElem
    for j in range(len(s)):
        sumVal += s[j]
        if signs[row][j + 1] == "+":
            if sumVal <= 0:
                return False
        elif signs[row][j + 1] == "-":
            if sumVal >= 0:
                return False
        else:
            if sumVal != 0:
                return False

    return True

def dfs(s, row):
    if len(s) == n:
        print(*s)
        return True

    if signs[row][0] == "+":
        # 해당 row의 첫성분으로써 i를 추가했다고 가정했을 때,
        for i in range(1, 11):
            # 해당 row의 나머지 부호들도 만족하는지 확인 (만족하지 못하면, 바로 loop를 종료하고 flag = False가 된다)
            if check(s, row, firstElem=i) == False:
                continue

            s.insert(0, i)
            isPrinted = dfs(s, row=row-1)
            # 만약 출력이 되었다면, 탐색을 전부 종료한다.
            if isPrinted == True:
                return True
            s.pop(0)
        # 만약 어떠한 i도 부호를 전부 만족할 수 없다면, 이 가지는 틀려먹었으므로 쳐낸다.
        return False

    elif signs[row][0] == "-":
        for i in range(-1, -11, -1):
            # 해당 row의 나머지 부호들도 만족하는지 확인 (만족하지 못하면, 바로 loop를 종료하고 flag = False가 된다)
            if check(s, row, firstElem=i) == False:
                continue

            s.insert(0, i)
            isPrinted = dfs(s, row=row - 1)
            # 만약 출력이 되었다면, 탐색을 전부 종료한다.
            if isPrinted == True:
                return True
            s.pop(0)
        # 만약 어떠한 i도 부호를 전부 만족할 수 없다면, 이 가지는 틀려먹었으므로 쳐낸다.
        return False
    # 해당 row의 첫번째 수가 0일 경우
    else:
        # 해당 row의 나머지 부호들도 만족하는지 확인 (만족하지 못하면, 바로 loop를 종료하고 flag = False가 된다)
        # 첫번째 성분으로 0을 넣었을 때 부호를 전부 만족할 수 없다면, 이 가지는 틀려먹었으므로 쳐낸다.
        if check(s, row, firstElem=0) == False:
            return False

        s.insert(0, 0)
        isPrinted = dfs(s, row=row - 1)
        # 만약 출력이 되었다면, 탐색을 전부 종료한다.
        if isPrinted == True:
            return True
        s.pop(0)

# 부호 표 보기 편하게 출력용!
# for sign in signs:
#     print(sign)
dfs(s=[], row=n-1)

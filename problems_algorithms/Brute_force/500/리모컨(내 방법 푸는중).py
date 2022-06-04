# https://www.acmicpc.net/problem/1107
# 문제점: bigger가 정확히 안구해짐
# 예시) 123456 8 2 3 4 5 6 7 8 9
# 문제점: smaller가 0 여러개가 나오기도 함
# 예시) 500000 9 1 2 3 4 5 6 7 8 9
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
if m != 0:
    banned = list(map(int, sys.stdin.readline().strip().split()))
else:
    banned = []

def findClosestNum(n, m, banned, initial):

    possible = [i for i in range(10) if i not in banned]
    if len(possible) == 0:
        return initial, initial
    numDigit = len(str(n)) # 목표값 n의 자리수 세기
    firstNum = int(str(n)[0]) # 목표값 n의 첫번째 자리수 값
    # 1) 목표값보다 더 큰 경우

    flag = 0 # 아직 동일한 값만 입력해왔으면 flag = 0, 다른 값을 입력했으면 flag = 1
    bigger = ""
    # 만약 가능한 숫자들 중에서, firstNum보다 한단계 큰 수가 없으면, 자리수를 하나 늘린 수가 선택된다
    if possible[-1] < firstNum:
        # possible의 첫성분이 0보다 클 경우
        if possible[0] != 0:
            bigger = str(possible[0])*(numDigit + 1)
        # possible의 첫성분이 0일 경우, possible이 0 말고 다른 성분도 가지고 있을 경우
        elif len(possible) > 1:
            bigger = str(possible[1]) + str(possible[0])*numDigit
        # possible 이 0 하나만 성분으로 가질 경우
        else:
            bigger = str(100000000) # 엄청 큰 수를 넣어버린다.
    # 만약 가능한 숫자들 중에서, firstNum보다 한단계 큰 수가 있으면, 같은 자리수의 수로 선택된다
    else:
        for num in list(map(int, str(n))):
            # 이미 한 번 한단계 큰 수가 입력된 상태라면, possible에서 가장 작은 수만 입력해간다.
            if flag == 1:
                bigger += str(possible[0])
            # 동일한 숫자가 possible에 존재하면, 동일한 수를 입력한다.
            elif num in possible:
                bigger += str(num)
            # 동일한 숫자가 possible에 존재하지 않으면, 한단계 큰 수를 입력하거나, possible에서 가장 작은 수를 입력한다.
            # (이 때, 첫자리수는 적어도 한단계 큰 수는 존재한다. 즉 첫자리수는 isAdded = False 가 되진 않는다)
            else:
                isAdded = False
                # 한단계 큰 수를 입력하고, for loop를 빠져나온다.
                for i in possible:
                    if i > num:
                        bigger += str(i)
                        isAdded = True
                        break
                # 한단계 큰 수가 존재하지 않았을 경우, possible에서 가장 작은 수를 입력한다.
                if isAdded == False:
                    bigger += str(possible[0])
                flag = 1

    # 2) 목표값보다 더 작은 경우
    flag = 0  # 아직 동일한 값만 입력해왔으면 flag = 0, 다른 값을 입력했으면 flag = 1
    smaller = ""
    # 만약 가능한 숫자들 중에서, firstNum보다 한단계 작은 수가 없거나 0 1개밖에 없으면, 자리수를 하나 줄인 수가 선택된다
    if possible[0] >= firstNum:
        # 만약 1자리수면, 매우 작은 음수로 입력한다.
        if numDigit == 1:
            smaller = str(-100000000)
        else:
            smaller = str(possible[-1])*(numDigit - 1)

    # 만약 가능한 숫자들 중에서, firstNum보다 한단계 작은 수가 있으면, 같은 자리수의 수로 선택된다
    else:
        for num in list(map(int, str(n))):
            # 이미 한 번 한단계 작은 수가 입력된 상태라면, possible에서 가장 큰 수만 입력해간다.
            if flag == 1:
                smaller += str(possible[-1])
            # 동일한 숫자가 possible에 존재하면, 동일한 수를 입력한다.
            elif num in possible:
                smaller += str(num)
            # 동일한 숫자가 possible에 존재하지 않으면, 한단계 작은 수를 입력하거나, possible에서 가장 작은 수를 입력한다.
            # (이 때, 첫자리수는 적어도 한단계 작은 수는 존재한다. 즉 첫자리수는 isAdded = False 가 되진 않는다)
            else:
                isAdded = False
                # 한단계 작은 수를 입력하고, for loop를 빠져나온다.
                for i in range(len(possible) - 1, -1, -1):
                    if possible[i] < num:
                        smaller += str(possible[i])
                        isAdded = True
                        break
                # 한단계 작은 수가 존재하지 않았을 경우, possible에서 가장 큰 수를 입력한다.
                if isAdded == False:
                    smaller += str(possible[-1])
                flag = 1


    print("bigger: ", bigger, "smaller: ", smaller)
    return int(bigger), int(smaller)

initial = 100

# 1) 금지된 숫자버튼을 제외한 숫자버튼만 누른 뒤, +-버튼을 누르는 경우
# 숫자버튼으로 나올 수 있는 가장 가까운 수를 찾는다
bigger, smaller = findClosestNum(n, m, banned, initial)
# 숫자버튼으로 나올 수 있는 경우 2가지를 찾는다. 목표값보다 더 큰 수 & 목표값보다 더 작은 수
# 2가지의 수들 중, 절대값의 차이가 더 작은 수를 찾는다.

# ans1 = 그 수의 자리수 + 절대값의 차이
ans1 = len(str(bigger)) + abs(n - bigger)
ans2 = len(str(smaller)) + abs(n - smaller)

# 2) +-버튼만 누르는 경우
# initial 과의 절대값의 차이를 구한다.
ans3 = abs(n - initial)

# 출력값: min(ans1, ans2)
print(min(ans1, ans2, ans3))

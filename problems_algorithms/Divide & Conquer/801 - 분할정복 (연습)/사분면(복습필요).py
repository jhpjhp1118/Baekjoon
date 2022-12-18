# https://www.acmicpc.net/problem/1891
import sys

input = sys.stdin.readline

d, val = input().strip().split()
d = int(d)
val = list(map(int, list(val)))

x, y = list(map(int, input().strip().split()))

"""
아이디어: 
    1. 주어진 val --> xVal, yVal 좌표계로 변환
    2. xVal, yVal --> xVal + x, yVal + y 
    3. xVal, yVal --> 사분면 좌표로 변환

"""

global xVal, yVal
xVal, yVal = 0, 0

def val2xy(n, d, val):
    """
    n: 현재 사분면의 깊이 (몇 번이나 재귀호출했는지를 나타냄)
    """
    global xVal, yVal

    # val 의 마지막 사분면 위치까지 반영했을 때, 함수를 종료한다.
    if n == d:
        return
    # val[n]번째 사분면의 가장 왼쪽 위 칸의 좌표값으로 xVal & yVal을 갱신한다.
    if val[n] == 1:
        xVal += 2**(d - n - 1)
    elif val[n] == 2:
        pass
    elif val[n] == 3:
        yVal += 2**(d - n - 1)
    else:
        xVal += 2**(d - n - 1)
        yVal += 2**(d - n - 1)

    # 한 단계 작은 사분면의 위치를 반영하기 위해, 재귀호출한다.
    val2xy(n + 1, d, val)


def xy2val(d, xVal, yVal, xCurr, yCurr, result):
    """
    xCurr & yCurr: 현재 사분면 깊이에서, 가장 왼쪽 위 칸의 좌표값 
    """
    # 사분면 위치가 완성되면, 출력한 뒤 종료한다.
    if len(result) == d:
        print(result)
        exit()

    # 현재의 한 사분면 길이를 계산한다.
    length = 2**(d - len(result) - 1)

    # 현재 사분면 기준으로, 어떤 사분면에 위치했는지에 따라, xCurr & yCurr를 갱신하고, result 에 해당 사분면 값을 추가한다.
    if xVal < xCurr + length:
        if yVal < yCurr + length:
            result += "2"
        else:
            result += "3"
            yCurr += length
    else:
        xCurr += length
        if yVal < yCurr + length:
            result += "1"
        else:
            result += "4"
            yCurr += length

    # 한 단계 작은 사분면으로 재귀호출한다.
    xy2val(d, xVal, yVal, xCurr, yCurr, result)

# 1. 주어진 val --> xVal, yVal 좌표계로 변환
val2xy(0, d, val)

# 2. xVal, yVal --> xVal + x, yVal + y
xVal, yVal = xVal + x, yVal - y

# 3. xVal, yVal --> 사분면 좌표로 변환
# 옮겨진 칸의 위치가 좌표 범위를 넘어서지 않으면, 사분면 위치를 찾는다.
if 0 <= xVal < 2**d and 0 <= yVal < 2**d:
    xy2val(d, xVal, yVal, 0, 0, "")
# 범위를 벗어나면, -1을 출력한다.
else:
    print(-1)

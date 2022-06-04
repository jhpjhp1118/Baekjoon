# https://www.acmicpc.net/problem/1107
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
banned = list(map(int, sys.stdin.readline().strip().split()))

def findClosestNum(n, m, banned):
    pass

    return ClosestNum


initial = 100

# 1) 금지된 숫자버튼을 제외한 숫자버튼만 누른 뒤, +-버튼을 누르는 경우
# 숫자버튼으로 나올 수 있는 가장 가까운 수를 찾는다
ClosestNum = findClosestNum(n, m, banned)
# 숫자버튼으로 나올 수 있는 경우 2가지를 찾는다. 목표값보다 더 큰 수 & 목표값보다 더 작은 수
# 2가지의 수들 중, 절대값의 차이가 더 작은 수를 찾는다.

# ans1 = 그 수의 자리수 + 절대값의 차이
ans1 = len(str(ClosestNum)) + abs(ClosestNum- initial)

# 2) +-버튼만 누르는 경우
# initial 과의 절대값의 차이를 구한다.
ans2 = abs(n - initial)

# 출력값: min(ans1, ans2)

# https://www.acmicpc.net/problem/1744
import sys
input = sys.stdin.readline

n = int(input().strip())

ans = 0

positive = [] # 1 보다 큰 양수를 담는 리스트 생성
negative = [] # 음수를 담는 리스트 생성
isHaveZero = 0 # 주어진 수열이 0을 포함하고 있는지 여부

# 수열을 입력받고, 분류한다.
for _ in range(n):
    num = int(input().strip())
    # num 이 1일 경우, 바로 더한다. (리스트에 담지는 않는다)
    if num == 1:
        ans += num
    # num 이 0일 경우, 수열이 0을 포함하고 있다고 기록해둔다.
    elif num == 0:
        isHaveZero = True
    # num 이 1보다 큰 양수일 경우, positive에 추가한다.
    elif num > 0:
        positive.append(num)
    # num 이 음수일 경우, negative에 추가한다.
    else:
        negative.append(num)

# positive, negative를 각각 오름차순으로 정렬한다.
positive = sorted(positive)
negative = sorted(negative)

# positive 성분 최적으로 묶어서 더해주기
# positive 의 성분 갯수가 홀수일 경우, positive 의 첫 성분만 그대로 ans 에 더해준다.
if len(positive) % 2 == 1:
    ans += positive.pop(0)
# 나머지 성분들은 인접한 수끼리 묶어서 더해준다.
for i in range(len(positive) // 2):
    ans += positive[2 * i] * positive[2 * i + 1]

# negative 성분 최적으로 묶어서 더해주기
# negative 의 성분 갯수가 홀수일 경우,
if len(negative) % 2 == 1:
    # 0 을 성분으로서 가지고 있지 않다면, negative 의 마지막 성분만 그대로 ans 에 더해준다.
    # (만약 0 을 성분으로서 가지고 있다면, (negative 의 마지막 성분) * 0 을 해서 없앤다.)
    if not isHaveZero:
        ans += negative.pop(-1)
# 나머지 성분들은 인접한 수끼리 묶어서 더해준다.
for i in range(len(negative) // 2):
    ans += negative[2 * i] * negative[2 * i + 1]

# 답을 출력한다.
print(ans)



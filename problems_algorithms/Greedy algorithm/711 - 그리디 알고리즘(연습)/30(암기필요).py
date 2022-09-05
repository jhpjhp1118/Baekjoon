# https://www.acmicpc.net/problem/10610
import sys
input = sys.stdin.readline

"""
아이디어: 가장 큰 수에 대해서만 확인한다. (만약 어떤 수가 3의 배수면, 어떤 숫자 조합을 해도 그 수는 3의 배수이다)
        10의 배수인지 먼저 판단한다. --> 0이 있으면, 그 수는 10의 배수이다.
        3의 배수인지 판단한다. --> 모든 자리수의 합이 3의 배수이면, 그 수는 3의 배수이다.
        둘 다 만족하면, 가장 처음 나오는 수를 출력한다.
"""

nums = list(map(int, list(input().strip())))
# 숫자를 내림차순으로 정렬한다. (가장 큰 수의 숫자배열이 된다.)
nums = sorted(nums, reverse=True)
# 만약 0을 가지고 있지 않을 경우, 10의 배수가 나올 수 없으므로, 불가능하다고 출력한다.
if nums[-1] != 0:
    print(-1)
# 0을 가지고 있는 경우
else:
    # 자리수의 합을 계산한다.
    sum = 0
    for num in nums:
        sum += num
    # 자리수의 합이 3의 배수이면, 해당 수도 3의 배수이므로, 그 수를 출력한다.
    if sum % 3 == 0:
        print(int("".join(list(map(str, nums)))))
    # 자리수의 합이 3의 배수가 안되면, 어떻게 배열해도 3의 배수는 만들 수 없으므로, 불가능하다고 출력한다.
    else:
        print(-1)





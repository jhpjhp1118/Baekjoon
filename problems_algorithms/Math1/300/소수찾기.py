# https://www.acmicpc.net/problem/1978
import sys

n = int(sys.stdin.readline().strip())

nums = map(int, sys.stdin.readline().strip().split())
result = 0
for num in nums:
    if num == 1: # 1은 소수가 아니므로 스킵
        continue
    elif num == 2: # 2는 소수이므로 카운트
        result += 1
        continue
    else: # 1,2 보다 큰 수 --> 직접 하나씩 나눠가면서 소수인지 확인
        isSosoo = False
        for i in range(2, num):
            if num % i == 0: # num 보다 작은 수로 나눠떨어지면, 소수가 아니므로 바로 루프 탈출
                break
            elif i == num - 1: # 마지막 수로도 나눠떨어지지 않으면, 소수로 카운트
                isSosoo = True
        if isSosoo:
            result += 1

print(result)

# https://www.acmicpc.net/problem/1541
import sys

"""
아이디어: 처음으로 - 기호가 나올 때까진 전부 더하고, -가 나온 뒤로는 전부 뺀다.
"""

# 수식을 입력받고, - 기호를 기준으로 구간을 나눈다.
sects = sys.stdin.readline().strip().split("-")

# 첫 구간의 숫자는 전부 더해준다.
ans = 0
nums = sects[0].split("+")
for num in nums:
    ans += int(num)

# 나머지 구간의 숫자는 전부 빼준다.
for sect in sects[1:]:
    nums = sect.split("+")
    for num in nums:
        ans -= int(num)

# 출력한다.
print(ans)






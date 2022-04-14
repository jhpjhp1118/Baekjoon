# https://www.acmicpc.net/problem/10820
import sys

while True:
    line = sys.stdin.readline().rstrip("\n")
    result = [0]*4

    # line이 주어지지 않을 경우, loop를 끝낸다.
    if not line:
        break

    for char in line:
        if char.isupper():
            result[1] += 1
        elif char.islower():
            result[0] += 1
        elif char.isnumeric():
            result[2] += 1
        elif char == " ":
            result[3] += 1

    print(*result)


# This is String
# SPACE    1    SPACE
#  S a M p L e I n P u T
# 0L1A2S3T4L5I6N7E8
# 자주쓰고, 같은 의미지만 더 효율적인 코드들 모음

# 숫자 입력 받기
# n = int(input())
import sys

n = int(sys.stdin.readline())

# sys.stdin.readline() 을 쓰면, 마지막에 개행문자 '\n'이 붙게 됨 --> 제거 필요
# 제거법: sys.stdin.readline().strip()

#

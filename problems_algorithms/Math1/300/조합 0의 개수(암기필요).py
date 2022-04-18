# https://www.acmicpc.net/problem/2004
import sys

# n!가 2의 몇 거듭제곱을 포함하고 있는지 확인하는 함수
def count_two(n):
    two = 0
    # 매 루프마다, 2^(i) 의 개수만큼 two에 더해진다 (two += n)
    # ex) 8! --> 8~1 중 (2^1의 배수의 개수 4개), (2^2의 배수의 개수 2개), (2^3의 배수의 개수 1개) --> 7개
    while n != 0:
        n = n // 2
        two += n
    return two

def count_five(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

n, r = map(int, sys.stdin.readline().strip().split())
print(min(count_two(n) - count_two(n -r) - count_two(r), count_five(n) - count_five(n -r) - count_five(r)))

# 조합 = (n * n-1 * ... * n-r+1) / r!

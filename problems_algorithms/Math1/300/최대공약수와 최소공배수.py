# https://www.acmicpc.net/problem/2609
import sys


# 유클리드 호제법
# a & b의 최대공약수: a를 b로 나눈 나머지 --> 나머지로 b 를 나눈 나머지 --> (나머지가 0이 될 때까지 반복)
# --> 나머지가 0이 될 때, 나눠지는 수가 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a%b

    return a


# a & b의 최소공배수: a * b / 최대공약수
def lcm(a, b):
    return a*b//gcd(a,b)


a, b = map(int, sys.stdin.readline().strip().split())

print(gcd(a, b), lcm(a, b), sep="\n")

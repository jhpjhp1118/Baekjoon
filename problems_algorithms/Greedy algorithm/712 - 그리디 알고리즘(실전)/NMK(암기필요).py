# https://www.acmicpc.net/problem/1201
import sys

input = sys.stdin.readline

"""
아이디어: m, k가 주어져있을 때, 해당 조건을 만족하는 n의 범위는 m + k - 1 <= n <= m * k

"""


n, m, k = list(map(int, input().strip().split()))




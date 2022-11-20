# https://www.acmicpc.net/problem/10816
import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().strip().split()))

m = int(input())
nums = list(map(int, input().strip().split()))

cards = sorted(cards)

# 딕셔너리를 이용하여, cards의 각 숫자의 개수를 미리 세어놓는다.
counts = {}
for card in cards:
    if card in counts:
        counts[card] += 1
    else:
        counts[card] = 1

# 이분 탐색을 통해, 해당 숫자의 존재여부를 판단한다. & 그 개수를 출력한다.
for i, num in enumerate(nums):
    low, high = 0, n - 1
    freq = 0 # cards에 존재하는 num의 개수
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] < num:
            low = mid + 1
        elif cards[mid] > num:
            high = mid - 1
        else:
            # num값이 cards에 존재할 경우, 그것의 (미리 세어놓은) 개수를 freq에 할당한다
            freq = counts[num]
            break

    # result에 num의 개수를 기록한다.
    print(freq, end=" ")

##########################################################################
# lower bound & upper bound를 이용한 또다른 풀이
# 중복값이 있을 때, 왼쪽 끝 index를 찾는 함수
# def lower_bound(cards, num):
#     low, high = 0, len(cards) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if cards[mid] < num:
#             low = mid + 1
#         elif cards[mid] > num:
#             high = mid - 1
#         elif cards[mid] == num:
#             if high == mid:
#                 return mid
#             high = mid
#
#     if cards[mid] == num:
#         return mid
#     else:
#         return -1
#
# # upper 가 맨 끝 index일 때, 정답을 못찾음!!
# # 중복값이 있을 때, 오른쪽 끝 index를 찾는 함수
# def upper_bound(cards, num):
#     low, high = 0, len(cards) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if cards[mid] < num:
#             low = mid + 1
#         elif cards[mid] > num:
#             high = mid - 1
#         elif cards[mid] == num:
#             if low == mid:
#                 if cards[high] == num:
#                     return high
#                 else:
#                     return mid
#             low = mid
#
#     if cards[mid] == num:
#         return mid
#     else:
#         return -1
#
# for i, num in enumerate(nums):
#     lower = lower_bound(cards, num)
#
#     if lower == -1:
#         print(0, end=" ")
#     else:
#         upper = upper_bound(cards, num)
#         print(upper - lower + 1, end=" ")
        
##########################################################################

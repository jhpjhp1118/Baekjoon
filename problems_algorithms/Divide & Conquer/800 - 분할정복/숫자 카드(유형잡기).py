# https://www.acmicpc.net/problem/10815
import sys
"""
아이디어: 효율적인 탐색 방법인 이진 탐색으로 하나씩 확인한다. 
이 때, 탐색하고자 하는 리스트의 정렬이 필수다
"""
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().strip().split()))

m = int(input())
nums = list(map(int, input().strip().split()))
##########################################################################
# cards를 크기순으로 정렬한다.
cards = sorted(cards)

result = [0]*m
# nums의 각 숫자들에 대해, cards 안에 해당 num이 있는지 확인한다. (이진탐색)
for i, num in enumerate(nums):
    # 첫 index & 마지막 index로 low & high 초기화
    low, high = 0, n - 1
    exist = False # num이 cards에 존재하는지 여부
    # low 가 high보다 작을 때까지만 반복한다.
    while low <= high:
        # 중간지점 index 정의한다.
        mid = (low + high) // 2
        # 만약 mid에 위치한 숫자카드값이 num보다 작을 경우,
        if cards[mid] < num:
            # 다음 step에서, mid보다 한 칸 오른쪽의 숫자카드 ~ high까지의 숫자카드를 탐색한다.
            low = mid + 1
        # 만약 mid에 위치한 숫자카드값이 num보다 클 경우,
        elif cards[mid] > num:
            # 다음 step에서, low ~ mid보다 한 칸 왼쪽의 숫자카드를 탐색한다.
            high = mid - 1
        # 만약 mid에 위치한 숫자카드값이 num과 일치할 경우,
        else:
            # 해당 num값의 숫자카드가 존재한다고 간주하고, 루프를 종료한다.
            exist = True
            break
    # 숫자카드 존재 여부에 따라, result 를 수정한다.
    if exist:
        result[i] = 1

# result 를 출력한다.
print(*result)

##########################################################################
# dictionary를 이용한 또다른 풀이
# dic = {}
# for card in cards:
#     dic[card] = 0
#
# result = [0]*m
# for i, num in enumerate(nums):
#     if num in dic:
#         result[i] = 1
#
# print(*result)
##########################################################################
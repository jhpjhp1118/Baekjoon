# https://www.acmicpc.net/problem/2751
# Time Complexity: O(nlogn)
n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

# 내장 함수
# num = sorted(num)

# 직접 구현
def merge_sort(array):

    # 재귀함수 종료 조건
    if len(array) <= 1:
        return array
    # 2개의 배열로 분할하기
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0, 0, 0

    while i < len(left) and j < len(right):
        # 2개의 배열을 하나의 배열로 합치면서 정렬하기
        if left[i] < right[j]:  # left의 해당성분이 더 작을 때
            array[k] = left[i]
            i += 1
        else:   # right 의 해당성분이 더 작을 때
            array[k] = right[j]
            j += 1
        k += 1
    # left 성분은 이미 모두 포함되었을 때, right 남은 성분들을 넣는다
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    # right 성분은 이미 모두 포함되었을 때, left 남은 성분들을 넣는다
    if j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

num = merge_sort(num)

# 출력
for i in num:
    print(i, end="\n")
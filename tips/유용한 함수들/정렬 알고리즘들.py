# 참고링크: https://dev-dain.tistory.com/113
"""
시간복잡도별로 다양한 정렬 알고리즘을 구현했다.
"""

import heapq

########################################################
"""
1. 선택 정렬
    - 가장 왼쪽부터 차례로 (현재 남아있는) 가장 작은 값을 위치시키는 방식
    - 시간복잡도: O(n^2)
"""
def solution1(l):
    # 0 ~ 마지막에서 2번째 성분까지...
    for i in range(len(l) - 1):
        # 초기화. (min_dix: 남은 성분들 중, 가장 작은 성분의 index)
        min_idx = i

        # min_idx를 가장 작은 성분의 index로 만들어준다.
        for j in range(i + 1, len(l)): # 남은 성분들 중에서...
            # 만약 현재의 min_idx의 성분보다 작은 성분이 발견되면,
            if l[min_idx] > l[j]:
                # min_idx 를 그 성분의 idx로 바꿔준다.
                min_idx = j

        # i번째 성분 <--> min_idx의 성분을 서로 맞바꿔준다.
        l[i], l[min_idx] = l[min_idx], l[i]

########################################################
"""
2. 삽입 정렬
    - 왼쪽에서 2번째 성분부터 차례로, 자기보다 왼쪽에 있는 수 배열에서, 
      적절한 자리를 내기 위해 기존 수들을 밀어내고, 그 적절한 자리에 삽입되는 방식
    - 시간복잡도: O(n^2)
"""
def solution2(l):
    # 1번 index부터 끝까지...
    for i in range(1, len(l)):
        # key <-- 현재 i번째 성분으로 초기화한다.
        key = l[i]
        # j <-- i - 1로 초기화한다.
        j = i - 1

        # <key가 들어가야 할 자리를 만들어주는 과정>
        # j가 list의 index 범위 안에 있고 & j번째 성분이 i번째 성분보다 크다면...
        while j >= 0 and l[j] > key:
            # j + 1번째 성분 <-- j번째 성분으로 바꿔준다.
            l[j + 1] = l[j]
            # j를 한 칸 왼쪽으로 움직인다.
            j -= 1

        # key가 들어가야 할 자리에 key를 넣어준다.
        l[j + 1] = key

########################################################
"""
3. 거품 정렬
    - 인접한 두 성분을 비교해서 차례로 정렬해주는 방식
        - 한 번 i 루프를 돌 때마다, 
          (남아있는 성분 & 자리에서)가장 오른쪽에 가장 큰 성분이 위치하게 된다.
    - 시간복잡도: O(n^2)
"""
def solution3(l):
    # l의 총 성분 개수 - 1 번 만큼 반복한다...
    # (n - 1 번만큼 정렬하면, 나머지 1개 성분은 자동으로 정렬되어있는 상태다)
    for i in range(len(l) - 1):
        # (정렬이 아직 확실하게는 안 된 성분 개수 - 1)만큼 반복한다...
        for j in range(len(l) - 1 - i):
            # 인접한 두 성분을 비교해서, 왼쪽 성분이 더 크면, 서로 맞바꿔준다.
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

########################################################
"""
4. 병합 정렬
    - 재귀적으로, 2개의 배열로 나눠 정렬한 뒤 병합하는 방식
    - 시간복잡도: O(nlogn)
"""
def solution4(l):
    # 정렬할 리스트의 성분 개수가 1 이하면 정렬할 필요 없다
    if len(l) <= 1:
        return

    # 절반을 나눠, 2개의 그룹으로 나눈다.
    mid = len(l) // 2
    g1 = l[:mid]
    g2 = l[mid:]

    # 각각의 그룹을 정렬한다. (recursion)
    solution4(g1)
    solution4(g2)

    # 초기화
    i1 = 0 # 그룹 1에서의 index
    i2 = 0 # 그룹 2에서의 index
    il = 0 # 결과 리스트에서의 index

    # i1 & i2 둘 다 각각의 그룹 index 범위 안에 있는 동안...
    while i1 < len(g1) and i2 < len(g2):
        # 만약 그룹 1의 현재 성분이 그룹 2의 현재 성분보다 작다면,
        if g1[i1] < g2[i2]:
            # 결과 리스트의 현재 성분 <-- 그룹 1의 현재 성분으로 채운다.
            l[il] = g1[i1]
            # i1을 한 칸 오른쪽으로 옮긴다.
            i1 += 1
        # 만약 반대일 경우,
        else:
            # 결과 리스트의 현재 성분 <-- 그룹 2의 현재 성분으로 채운다.
            l[il] = g2[i2]
            # i2를 한 칸 오른쪽으로 옮긴다.
            i2 += 1
        
        # il을 한 칸 오른쪽으로 옮긴다.
        il += 1
    
    # 둘 중 한 그룹이라도 아직 결과 리스트에 못 채워넣은 성분이 남아있을 경우, 채운다.
    while i1 < len(g1):
        l[il] = g1[i1]
        i1 += 1
        il += 1
    while i2 < len(g2):
        l[il] = g2[i2]
        i2 += 1
        il += 1

########################################################
"""
5. 퀵 정렬
    - pivot 값을 중심으로, 왼쪽에는 pivot보다 작은 값, 오른쪽에는 pivot보다 큰 값을
        놓는 규칙으로, 재귀적으로 정렬하는 방식
    - pivot을 효율적으로 정하는 방식이 제안되고 있다.
    - 시간복잡도: O(nlogn)
"""

def solution5(l, start, end):
    # 재귀 종료 조건: end가 start보다 안 클 경우
    if end - start <= 0:
        return

    # pivot 잡기
    pivotIdx = end # 여기는 다른 방식으로 변경 가능. 임의로 설정한 것
    # pivotIdx = (start + end) // 2
    pivot = l[pivotIdx]
    # i 초기화
    i = start
    # pivot보다 작은 성분들을 가장 왼쪽부터 차례대로 놓아준다.
    for j in range(start, end):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1 # for loop가 끝나면, i는 pivot의 위치가 된다.
    # pivot보다 한 단계 작은 수의 오른쪽에 pivot을 위치시킨다.
    l[i], l[pivotIdx] = l[pivotIdx], l[i]

    # pivot 기준으로 왼쪽 & 오른쪽 2개의 그룹을 정렬한다. (recursion)
    solution5(l, start, i - 1)
    solution5(l, i + 1, end)

# 퀵 소트를 호출하는 함수
def quick_sort(l):
    solution5(l, 0, len(l) - 1)


########################################################
"""
6. 힙 정렬
    - 힙의 특징을 이용하여, 정렬하는 방식
    - 최소 힙의 특징: 루트가 아닌 모든 노드는 부모 노드보다 크다.
    - heappush: 최소 힙이 되도록 성분을 추가한다.
    - heappop: 최소 힙에서 가장 작은 성분을 빼면서 return 한다.
    - heapq: 리스트를 최소 힙으로 다루도록 해주는 모듈
    - 시간복잡도: O(nlogn)
"""
def heap_sort(l):
    h = []
    for val in l:
        heapq.heappush(h, val)
    
    return [heapq.heappop(h) for _ in range(len(h))]

########################################################
# 결과 확인용
l = [2, 4, 5, 1, 3]
solution1(l)
# quick_sort(l)
# l = heap_sort(l)
print(l)


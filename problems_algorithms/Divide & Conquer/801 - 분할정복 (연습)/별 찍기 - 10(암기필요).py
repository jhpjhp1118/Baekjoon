# https://www.acmicpc.net/problem/2447
import sys
import math

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input().strip())

"""
아이디어:
    * 한 row씩 차례로 구성을 해서 출력해나간다 (메모리 아끼기 위함)
    * i번째 row --> n = 3^k 일 때, i를 3^(k - 1 ~ 0) 로 나눈 {몫}
                --> 몫을 3으로 나눈 나머지가 1일 때(=해당 깊이에서 비어야 하는 1번째 섹션이 비어야 하는 순서의 row일 경우),
                        해당 섹션은 전부 빈 칸으로!
                    - 위 조건에 해당 안되면, 해당 깊이에서 0번째 섹션을 복사해온다.
                --> 0번째 섹션은 한 깊이 더 깊게 재귀호출
    * 3등분되어있을 때, 0번째 섹션 = 2번째 섹션 복사해서 붙이기(
    * 재귀적으로 점점 깊어지는 방식으로 진행 (얕을수록 큰 섹션)
    
주의1) (0, 1, 2) 섹션 3개로 3등분했을 때: 0번째 섹션은 왼쪽, 1번째 섹션은 가운데, 2번째 섹션은 오른쪽
주의2) n = 243 일 때 이상함?! --> math.log(243) = 4.9999... --> int(4.9999...) = 4 이기 때문
            --> round() 로 해결
"""
# n 이 3의 몇 승인지 구하기
k = int(round(math.log(n, 3)))

global row


def generateRow(share, depth):
    """
    적절한 row를 생성하는 함수
    share: n = 3^k 일 때, i를 3^(k - 1 ~ 0) 로 나눈 {몫} 을 전부 담은 리스트
    depth: 재귀호출 깊이. 깊이가 얕을수록 기준 칸의 크기가 커진다.
    """
    global row
    # 최대 깊이를 초과했을 경우, 재귀를 종료한다.
    if depth == k + 1:
        return

    # 현재 깊이의 기준 길이를 미리 계산
    length = 3**(k - depth)

    # 0번째 섹션
    generateRow(share, depth + 1)

    # 1번째 섹션 - 깊이에 해당하는 몫을 3으로 나눈 나머지가 1일 때, 해당 깊이의 1번째 섹션을 전부 빈 칸으로 만든다.
    #          - 몫이 1이 아닐 때, 0번째 섹션 그대로 복사
    if share[depth - 1] % 3 == 1:
        row[length:2 * length] = [" "] * length
    else:
        row[length:2*length] = row[:length]

    # 2번째 섹션 <-- 0번째 섹션 그대로 복사
    row[2*length:3*length] = row[:length]


# 적절한 row를 1줄씩 출력한다.
for i in range(n):
    # 출력할 row 를 초기화한다. (일단 리스트의 형태로)
    row = ["*"]*n

    # i를 3^(k - 1 ~ 0) 로 나눈 {몫}을 미리 구한다.
    share = [i//(3**x) for x in range(k - 1, -1, -1)]

    # 재귀함수를 호출해서, 적절한 row를 생성한다.
    generateRow(share=share, depth=1)

    # row 를 string의 형태로 변환해서 출력한다.
    print("".join(row))



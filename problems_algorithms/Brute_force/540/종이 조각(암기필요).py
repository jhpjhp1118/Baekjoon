# https://www.acmicpc.net/problem/14391
import sys
# 참고 링크: https://lagooni.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%A2%85%EC%9D%B4-%EC%A1%B0%EA%B0%81-14391%EB%B2%88-Python-Bitmasking
n, m = list(map(int, sys.stdin.readline().strip().split()))

paper = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

ans = 0

# i번째 bitmask grid에 대해 탐색한다.
# 각 칸마다 0 & 1 2가지 값을 가질 수 있고, grid는 n*m 칸을 가지므로, 총 2^(n*m) 개의 경우를 탐색한다
# 2진법의 비트연산자를 쓰는 이유: 0과 1로만 이루어진 n*m개의 칸을 가지는 2진수가 있을 때, 이를 n by m 행렬로 바꾸면 grid가 된다.
# Ex) 000011 --> 000 / 011
# bitmask 규칙은 다음과 같이 정한다. --> 세로합을 해야되는 칸: 1, 가로합을 해야되는 칸: 0
for i in range(1 << n*m):
    total = 0
    # i번째 경우의 가로합만 전부 계산해서 total에 더해주기
    for row in range(n):
        rowsum = 0
        for col in range(m):
            idx = row*m + col
            # & 비트 연산자는, 각 자리수마다, 양쪽 값의 2진법 자리수가 전부 1일 때만 1이 나온다.
            # 1 << idx: 1, 10, 100, 1000, 10000, ...
            # i & (1 << idx): i번째 경우의 grid(=bitmask)에서, idx 위치의 값이 0이면, 무조건 0이 나오는 수식이다.
            # 가로합을 해야되는 성분이면, 이전까지의 합에 10을 곱해주고, 해당 성분을 더해준다.
            if i & (1 << idx) != 0:
                rowsum = 10*rowsum + paper[row][col]

            else:
                total += rowsum
                rowsum = 0
        total += rowsum
    # i번째 경우의 세로합을 전부 계산해서 total에 더해주기
    for col in range(m):
        colsum = 0
        for row in range(n):
            idx = row*m + col
            # 세로합을 해야되는 성분이면, 이전까지의 합에 10을 곱해주고, 해당 성분을 더해준다.
            if i & (1 << idx) == 0:
                colsum = 10*colsum + paper[row][col]

            else:
                total += colsum
                colsum = 0
        total += colsum
    
    # 최대값을 갱신한다.
    ans = max(ans, total)

print(ans)





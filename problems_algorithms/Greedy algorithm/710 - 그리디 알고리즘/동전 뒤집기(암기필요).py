# https://www.acmicpc.net/problem/1285
import sys
input = sys.stdin.readline

"""
아이디어: row를 뒤집을 수 있는 모든 경우에 대해, row를 뒤집어본 뒤, H보다 T가 더 많은 column을 뒤집어가며 ans를 갱신한다.
주의) pypy3로 해야함!
주의) 깊은 복사를 할 때, 계산속도는 copy.deepcopy > 슬라이싱
        --> 슬라이싱을 애용하자!
참고 링크) https://c4u-rdav.tistory.com/32
"""
n = int(input().strip())
coin = []
for _ in range(n):
    line = list(input().strip())
    coin.append(line)

def reverseRow(i, coinCopy):
    for j in range(n):
        if coinCopy[i][j] == "H":
            coinCopy[i][j] = "T"
        else:
            coinCopy[i][j] = "H"

# ans를 최악의 값으로 초기화한다.
ans = n ** 2
# bit: 어느 row를 미리 뒤집어 놓을지를 정해놓은 변수
# ex) 101: 1, 3번째 row를 뒤집음
for bit in range(1 << n):
    coinCopy = [coin[i][:] for i in range(n)]
    # bit에서 1로 표시되어 있는 row를 미리 다 뒤집어 놓는다.
    for i in range(n):
        if bit & (1 << i):
            reverseRow(i, coinCopy)

    # 모든 column에 대해, 최적의 T 갯수를 더해간다.
    val = 0
    for i in range(n):
        cnt = 0
        # T 갯수를 센다.
        for j in range(n):
            if coinCopy[j][i] == "T":
                cnt += 1
        # 현재 T 갯수 vs. 현재 H 갯수 중 더 작은 것을 더해간다. (T가 더 많으면, 뒤집으면 되므로)
        val += min(cnt, n - cnt)

    # ans를 갱신한다.
    ans = min(ans, val)
print(ans)


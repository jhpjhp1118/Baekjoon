# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

n, k = list(map(int, input().strip().split()))

# coin 입력받기
coins = []
for _ in range(n):
    coins.append(int(input().strip()))

# 큰 coin 부터 탐색할 수 있도록, 순서 뒤집어주기
coins = coins[::-1]
ans = 0 # coin 이용 개숫
# 큰 coin 부터 차례로 탐색한다.
for coin in coins:
    # 현재 coin이 하나라도 쓰일 수 있는 경우, 쓰인 coin 갯수를 count하고, 목표값까지 남은 k값으로 갱신한다.
    if k // coin != 0:
        ans += k // coin
        k %= coin
    # 목표값에 도달한 경우, 탐색을 종료한다.
    if k == 0:
        break
# 답을 출력한다.
print(ans)

# https://www.acmicpc.net/problem/2231
import sys
n = int(sys.stdin.readline().strip())

for i in range(1, n+1):
    if n == i + sum(map(int, str(i))):
        print(i)
        break
    # 생성자가 없을 때
    if i == n:
        print(0)
        break

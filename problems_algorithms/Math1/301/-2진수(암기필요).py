# https://www.acmicpc.net/problem/2089
import sys

N = int(sys.stdin.readline().strip())
ans = ''
if N == 0:
    print(0)
    exit()
while N != 0:
    if N % -2:
        N = N//-2 + 1 # -2진법의 경우, 나머지가 0이 아닐 때, 몫에 1을 더하고 진행한다!
        ans = '1'+ans
    else:
        N //= -2
        ans = '0'+ans
print(int(ans))

# 1 -2 4 -8 16 -32

# 5 = 4 + 1
# 6 = 16 - 8 - 2
# 7 = 16 - 8 - 2 + 1
# 10 = 16 - 8 + 4 - 2
# -13 = -32 + 16 + 4 - 2 + 1
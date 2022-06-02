# https://www.acmicpc.net/problem/1476
import sys
E_target, S_target, M_target = map(int, sys.stdin.readline().strip().split())

E, S, M = 1, 1, 1
ans = 1
while(True):
    if E == E_target and S == S_target and M == M_target:
        break

    E += 1
    S += 1
    M += 1
    ans += 1
    if E > 15:
       E = 1
    if S > 28:
       S = 1
    if M > 19:
       M = 1


print(ans)

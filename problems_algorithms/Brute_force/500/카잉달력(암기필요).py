# https://www.acmicpc.net/problem/6064
import sys

t = int(sys.stdin.readline().strip())
ks = []

# 정답을 k라 하면, (k-x) & (k-y) 둘 다 m의 배수이면서 n의 배수이다.
# k 후보를 하나씩 탐색한다. --> x에 m씩 더해가면, (k후보 - x) 는 무조건 m의 배수이다
#                       --> (k후보 - y)도 n의 배수인지 확인하고, 맞으면 그 수를 출력한다.
# ! 만약 1씩 더해서 가능한 모든 경우를 탐색완료 한다고 가정하면, k후보 = m*n이 된다.
#   --> 이 때까지 답이 안나오면, 가능한 모든 유효경우를 다 봤음에도 답이 없는 것이므로, 무효한 경우라고 판단한다.
for i in range(t):
    m, n, x, y = map(int, sys.stdin.readline().strip().split())
    flag = 0 # 유효한 경우면 1, 무효한 경우면 0
    k = x
    while k <= m*n:
        if (k - y)%n == 0:
            flag = 1
            break
        k += m

    if flag == 0:
        k = -1

    ks.append(k)
for i in ks:
    print(i)

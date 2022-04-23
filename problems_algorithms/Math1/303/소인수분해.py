# https://www.acmicpc.net/problem/11653
import sys

n_max = 10000000
n_max_r = int(n_max**0.5) # 천만은 너무 크므로, 천만의 제곱근만큼 탐색한다. (제곱근까지 인수가 안나오면, 소수라는 성질 이용)
check = [False, False] + [True] * n_max_r

# 각 index에 해당하는 수가 소수인지/아닌지 판별해놓은 리스트 생성
for i in range(2, int(n_max_r**0.5) + 1):
    if check[i]:
        for j in range(i + i, n_max_r + 1, i):
            check[j] = False
# 소수만 모아놓은 리스트 생성
prime = [x for x in range(len(check)) if check[x] == True]

n = int(sys.stdin.readline().strip())
# 탐색구간 내의 모든 소수에 대해 탐색
for i in prime:
    if i > n: # n이 인수 후보보다 작으면, 탐색을 종료한다.
        if n > 1: # n 이 소수이면, 출력한다. (완전히 나누어떨어졌을 경우, n=1이거나/n=(prime의 가장 큰 소수보다 큰 수).)
            print(n)
        break
    while n%i == 0: # 인수가 나오면, 안 나누어떨어질 때까지 나누면서 출력한다.
        n //= i
        print(i)

if n > prime[-1]: # prime의 가장 큰 수보다 크면, 무조건 소수이다 --> 출력한다.
    print(n)
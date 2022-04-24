# https://www.acmicpc.net/problem/9095
import sys

# n의 경우의 수는,
# 1) n-1의 경우의 수에다가, 오른쪽 끝에 +1 추가하기
# 2) n-2의 경우의 수에다가, 오른쪽 끝에 +2 추가하기
# 3) n-3의 경우의 수에다가, 오른쪽 끝에 +3 추가하기

result = [0, 1, 2, 4] # 각각 n=0,1,2,3 인 경우의 수 (n=0은 사실상 무의미)
# n=3: 1+1+1, 1+2, 2+1, 3 --> 총 4개

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())

    for i in range(len(result), n+1): # result에 추가 안되어 있는 경우면, n번째 경우가 추가될 때까지 경우의 수를 추가한다.
        result.append(result[i-1] + result[i-2] + result[i-3])
    print(result[n])

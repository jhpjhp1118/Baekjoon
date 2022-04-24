# https://www.acmicpc.net/problem/11727
import sys

# n의 경우의 수는,
# 1) n-2의 경우에다가, = 모양으로 1*2 블록을 2개 오른쪽 끝에 추가하기 + ㅁ 모양으로 2*2 블록을 1개 오른쪽 끝에 추가하기
# 2) n-1의 경우에다가, | 모양으로 2*1 블록을 1개 오른쪽 끝에 추가하기
# 위의 2가지를 합친 것

n = int(sys.stdin.readline().strip())
result = [0, 1, 3] # n=0, 1, 2 일 때에 해당하는 각각의 경우의 수(n=0은 사실상 무의미한 데이터)

for i in range(3, n+1):
    result.append(result[i-1] + 2*result[i-2])

print(result[n]%10007)


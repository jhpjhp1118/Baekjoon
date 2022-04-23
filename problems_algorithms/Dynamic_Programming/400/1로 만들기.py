# https://www.acmicpc.net/problem/1463
import sys

n = int(sys.stdin.readline().strip())
result = [0]*(n + 1) # 각 수에 대해, 최적 연산횟수를 저장한 리스트. 0과 1(리스트에서 1,2번째 성분) 은 무시된다.

for i in range(2, n + 1):
    # 아래의 " + 1" 은 연산횟수를 1만큼 더한다는 것을 뜻한다.
    result[i] = result[i - 1] + 1 # 1을 빼는 연산이 최선인 경우
    if i % 3 == 0:
        result[i] = min(result[i], result[i//3] + 1)
    if i % 2 == 0:
        result[i] = min(result[i], result[i//2] + 1)

print(result[n])

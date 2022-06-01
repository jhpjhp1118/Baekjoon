# https://www.acmicpc.net/problem/13398
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))

# 2개의 row를 가진 result 배열 생성하기
# 1번째 row: 원소를 1개도 제거하지 않을 때, 최대 연속합을 구하는 행
# 2번째 row: 원소를 1개 제거할 때, 최대 연속합을 구하는 행
result = [[0]*n for _ in range(2)]
result[0][0] = data[0]

if n > 1:
    # 최종 답은 절대 처음 data 값보다 작을 수 없으므로, 처음 data 값으로 초기값을 정한다.
    ans = data[0]
    for i in range(1, n):
        # 기존 연속합 방식과 동일
        result[0][i] = max(result[0][i-1] + data[i], data[i])
        # 원소를 1개 제거하는 경우는 2가지가 있다 --> 이 2가지 중 더 큰 값을 기록한다.
        # 1) i번째 data 값을 제거할 경우: result[0][i-1] 에다가 data[i]를 더하지 않으면 된다.
        # 2) 이미 1개의 data 값을 제거한 경우: 더 data 값을 제거할 수 없으므로, 이미 제거한 값을 저장한 result[1][i-1]에
        #                                   data[i]를 더하면 된다.
        result[1][i] = max(result[0][i-1], result[1][i-1] + data[i])
        # 그냥 result의 최대값을 구하면 안됨! <-- 모든 data 값이 음수일 경우, result[1][0] = 0임. 이러면 틀린 답인 0이 출력됨.
        ans = max(ans, result[0][i], result[1][i])
    print(ans)
else:
    print(result[0][0])




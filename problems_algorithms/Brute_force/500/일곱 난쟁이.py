# https://www.acmicpc.net/problem/2309
import sys
data = []
for _ in range(9):
    data.append(int(sys.stdin.readline().strip()))

sum_val = sum(data)
flag = 0
bad_guys = []
for i in range(9):
    for j in range(i+1, 9):
        # i & j 번째 값을 제외한, 나머지 값들의 합 = 100인 경우를 찾는다
        if sum_val - (data[i] + data[j]) == 100:
            # 나쁜 놈들을 기록한다.
            bad_guys.append(data[i])
            bad_guys.append(data[j])
            flag = 1
            break
    if flag == 1:
        break
# 나쁜 놈들을 제거한다.
data.remove(bad_guys[0])
data.remove(bad_guys[1])

# data를 오름차순으로 정렬시킨다.
data = sorted(data)

# 순서대로 한줄씩 출력한다.
for val in data:
    print(val)

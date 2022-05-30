# https://www.acmicpc.net/problem/9465
import sys

t = int(sys.stdin.readline().strip())
show = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    data = []
    for _ in range(2):
        data.append(list(map(int, sys.stdin.readline().strip().split())))

    # i = 0
    result = [[0, 2]]
    # i = 1
    compare = [data[0][0], data[1][0]]
    if compare[0] != compare[1]:
        result.append([max(compare), compare.index(max(compare))])
    else:
        result.append([max(compare), 2])

    if n > 1:
        # i = 2 ~ n
        for i in range(2, n+1):
            compare = [data[0][i-1], data[1][i-1]]
            compare_case = []

            # 1)
            # print(result)
            compare_case.append(result[i-2][0] + max(compare)) # 요기! 1) case 에 대한 index가 조사가 안됨

            # 2)
            if result[i-1][1] == 2:
                value_append = data[result[i - 2][1]][i-1] # 요기! 연속으로 data가 같으면, 오류 뜸
            else: # result[i-1][1] = 0 or 1
                value_append = data[1 - result[i - 1][1]][i-1]
            compare_case.append(result[i - 1][0] + value_append)
            # print("compare_case:", compare_case)

            index = compare.index(value_append)
            if compare[0] == compare[1]:
                result.append([max(compare_case), 2])
            else:
                result.append([max(compare_case), index])

    show.append(result[n][0])

for i in range(t):
    print(show[i])
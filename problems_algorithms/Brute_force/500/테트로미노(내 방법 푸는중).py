# https://www.acmicpc.net/problem/14500
import sys
# ??? 왜 내 brute force 방법은 계산시간이 초과되지?? 기본적인 원리는 dfs 모범답안과 동일한데?
n, m = map(int, sys.stdin.readline().strip().split())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))
max_val = max(map(max, data)) # 최대값 구하기
steps = [[1,0], [0,1], [-1,0], [0,-1]]
ans = -1
for i in range(n):
    for j in range(m):
        checker = [[0] * m for _ in range(n)]
        checker[i][j] = 1

        newSum = data[i][j]
        if ans >= newSum + max_val*3:
            continue
        for step1 in steps:
            pos1 = [i + step1[0], j + step1[1]]
            if 0 <= pos1[0] < n and 0 <= pos1[1] < m and checker[pos1[0]][pos1[1]] == 0:
                newSum += data[pos1[0]][pos1[1]]
                if ans >= newSum + max_val * 2:
                    newSum -= data[pos1[0]][pos1[1]]
                    continue
                checker[pos1[0]][pos1[1]] = 1
                for step2 in steps:
                    pos2 = [pos1[0] + step2[0], pos1[1] + step2[1]]
                    if 0 <= pos2[0] < n and 0 <= pos2[1] < m and checker[pos2[0]][pos2[1]] == 0:
                        newSum += data[pos2[0]][pos2[1]]
                        if ans >= newSum + max_val * 1:
                            newSum -= data[pos2[0]][pos2[1]]
                            continue
                        checker[pos2[0]][pos2[1]] = 1
                        for step3 in steps:
                            # 뻐큐모양 아닌 거
                            pos3 = [pos2[0] + step3[0], pos2[1] + step3[1]]
                            if 0 <= pos3[0] < n and 0 <= pos3[1] < m and checker[pos3[0]][pos3[1]] == 0:
                                newSum += data[pos3[0]][pos3[1]]
                                checker[pos3[0]][pos3[1]] = 1
                                ans = max(ans, newSum)
                                newSum -= data[pos3[0]][pos3[1]]
                                checker[pos3[0]][pos3[1]] = 0
                            # 뻐큐모양
                            pos3 = [pos1[0] + step3[0], pos1[1] + step3[1]]
                            if 0 <= pos3[0] < n and 0 <= pos3[1] < m and checker[pos3[0]][pos3[1]] == 0:
                                newSum += data[pos3[0]][pos3[1]]
                                checker[pos3[0]][pos3[1]] = 1
                                ans = max(ans, newSum)
                                newSum -= data[pos3[0]][pos3[1]]
                                checker[pos3[0]][pos3[1]] = 0
                        newSum -= data[pos2[0]][pos2[1]]
                        checker[pos2[0]][pos2[1]] = 0

                newSum -= data[pos1[0]][pos1[1]]
                checker[pos1[0]][pos1[1]] = 0

print(ans)





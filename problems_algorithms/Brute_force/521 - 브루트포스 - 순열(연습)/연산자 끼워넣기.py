# https://www.acmicpc.net/problem/14888
import sys

n = int(sys.stdin.readline().strip())

vals = list(map(int, sys.stdin.readline().strip().split()))
operNums = list(map(int, sys.stdin.readline().strip().split()))

# 최대값, 최소값 후보 초기화
global ans_max, ans_min
ans_max = -1e9
ans_min = 1e9

def dfs(opers, result, idx):
    global ans_max, ans_min
    # 사용한 부호의 갯수들이, 주어진 부호 갯수들과 같을 경우, ans_max & ans_min 을 갱신한다
    if opers == operNums:
        if ans_max < result:
            ans_max = result
        if ans_min > result:
            ans_min = result
        return


    for i in range(4):
        if opers[i] + 1 <= operNums[i]:
            if i == 0: # 덧셈
                dfs(opers=[opers[0] + 1, opers[1], opers[2], opers[3]], result=result + vals[idx], idx=idx + 1)

            elif i == 1: # 뺄셈
                dfs(opers=[opers[0], opers[1] + 1, opers[2], opers[3]], result=result - vals[idx], idx=idx + 1)
            elif i == 2: # 곱셈
                dfs(opers=[opers[0], opers[1], opers[2] + 1, opers[3]], result=result * vals[idx], idx=idx + 1)
            else: # 나눗셈
                if result < 0:
                    dfs(opers=[opers[0], opers[1], opers[2], opers[3] + 1],
                        result=-(abs(result) // vals[idx]), idx=idx + 1)
                else:
                    dfs(opers=[opers[0], opers[1], opers[2], opers[3] + 1],
                        result=result // vals[idx], idx=idx + 1)


dfs(opers=[0, 0, 0, 0], result=vals[0], idx=1)
print(ans_max)
print(ans_min)





# https://www.acmicpc.net/problem/1062
import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))

# a, c, i, n, t --> 최소 5개 알파벳 필요하므로, K가 이보다 적으면 아무것도 읽을 수 없다
if K < 5:
    print(0)
    exit()

if K == 26:
    print(N)
    exit()

# 단어들 입력받기
words = [set(sys.stdin.readline().strip()) for _ in range(N)]

# 배운 알파벳을 표시하는 리스트
learn = [0]*26

# "anta" & "tica" 를 꼭 읽기 위한 알파벳들은 필수로 익히기
for char in ["a", "c", "i", "n", "t"]:
    learn[ord(char) - ord("a")] = 1

ans = 0

def dfs(idx, cnt):
    global ans
    # 만약 익힌 알파벳 갯수 == K - 5 개 일 경우, 읽을 수 있는 단어 개수를 세서 갱신한다.
    if cnt == K - 5:
        num = 0
        # 모든 주어진 단어들에 대해,
        for word in words:
            isReadable = True
            # 한 단어의 모든 알파벳에 대해,
            for char in word:
                # 배우지 않은 알파벳이 하나라도 있으면, 읽지 못하는 단어로 간주하고 skip 한다.
                if learn[ord(char) - ord("a")] == 0:
                    isReadable = False
                    break

            if isReadable:
                num += 1

        ans = max(ans, num)

        return

    for i in range(idx, 26): # 직전에 배운 알파벳보다 뒤에 위치한 알파벳들만 탐색한다.
        # 만약 아직 배우지 않은 알파벳이라면, 탐색의 대상이 된다.
        if learn[i] == 0:
            learn[i] = 1
            dfs(i, cnt + 1)
            learn[i] = 0


dfs(0, 0)
print(ans)

# https://www.acmicpc.net/problem/14226
import sys
from collections import deque

s = int(sys.stdin.readline().strip())

# clipboard = 0
# 각 row의 1번째 값: 최소 동작 횟수, 2번째 값: clipboard 속 이모티콘 갯수
visited = [[-1, 0] for _ in range(2001)]

def action(num, opt):
    # 이모티콘 하나 삭제하기
    if opt == 1:
        # clipboard = visited[num][1]
        num -= 1 # 이모티콘 하나 삭제하기
        # visited[num][1] = clipboard # clipboard 는 그대로 유지됨을 기록해줌
        # print("option 1")
    # 클립보드의 이모티콘들 붙여넣기
    elif opt == 2: 
        clipboard = visited[num][1]
        num += clipboard # 이모티콘 붙여넣기
        # visited[num][1] = clipboard # clipboard 는 그대로 유지됨을 기록해줌
        # print("option 2")
    # 클립보드에 전체 복사하기
    else: 
        visited[num][1] = num
        # print("option 3")       
    
    return num 

num = 1
visited[num][0] = 0

q = deque([num])

while q:
    now = q.popleft()

    for opt in range(1, 4):
        val = action(now, opt)
        
        # 범위를 너무 많이 넘어서면, skip한다.
        if val <= 0 or val > 2001:
            continue    
        
        # 이미 방문한 갯수이면, skip한다.
        if opt != 3 and visited[val][0] != -1:
            continue
        print("opt:", opt, "now:", now, "val:", val)
        visited[val][0] = visited[now][0] + 1
        visited[val][1] = visited[now][1]

        if val == s:
            print(visited[val][0])
            exit()

        q.append(val)

# 반례: 872 --> 22
# https://www.acmicpc.net/board/view/30100


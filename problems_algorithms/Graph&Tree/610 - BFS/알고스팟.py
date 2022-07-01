# https://www.acmicpc.net/problem/1261
import sys
from collections import deque
import copy

"""
아이디어: 특정 칸까지 가는데 있어서, 뚫고 가야하는 최소한의 벽의 갯수를 bfs 탐색해가며 기록해나간다.
"""

m, n = list(map(int, sys.stdin.readline().strip().split()))

maze = []
for _ in range(n):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]

visited = [[-1]*m for _ in range(n)]
visited[0][0] = 0

q = deque()
q.append((0, 0)) 
qNext = deque()
flag = False

if n == 1 and m == 1:
    print(0)
    exit()


while True:
    while q:
        r, c = q.popleft()

        for step in steps:
            rt, ct = r + step[0], c + step[1]

            if rt < 0 or rt >= n or ct < 0 or ct >= m:
                continue

            if rt == n - 1 and ct == m - 1:
                flag = True

            if visited[rt][ct] == -1:
                if maze[rt][ct] == 1:
                    visited[rt][ct] = visited[r][c] + 1
                else:
                    visited[rt][ct] = visited[r][c]
                
                qNext.append((rt, ct))
            
            else:
                if maze[rt][ct] == 1:
                    compare = visited[r][c] + 1
                else:
                    compare = visited[r][c]
                
                if visited[rt][ct] <= compare:
                    continue
                else:
                    visited[rt][ct] = compare
                    qNext.append((rt, ct))

    if flag:
        print(visited[n - 1][m - 1])
        for row in visited:
            print(row)
        exit()
    
    q = copy.deepcopy(qNext)

    qNext = deque()
            
            
"""
반례) 정답 1
6 5
001011
110100
100110
101000
000010
"""





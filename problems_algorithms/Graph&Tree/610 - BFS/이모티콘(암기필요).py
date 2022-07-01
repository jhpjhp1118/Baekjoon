# https://www.acmicpc.net/problem/14226
import sys
from collections import deque
# 참고링크: https://velog.io/@aonee/%EB%B0%B1%EC%A4%80-boj-14226-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
아이디어: 2차원 배열에 1) 현재 이모티콘 갯수 2) 그 이모티콘 갯수가 될 때의 클립보드 속 이모티콘 갯수
            인 경우에 해당하는 "최소 이동 횟수"를 기록해가면서 bfs를 진행한다.
"""
s = int(sys.stdin.readline().strip())

dist = [[-1]*1001 for _ in range(1001)]

q = deque()
q.append((1, 0))
dist[1][0] = 0

while q:
    num, c = q.popleft()

    # if문에서 dist[~][~] == -1 인지 확인하는 것: 한번도 방문안했는지 확인하는 용도.

    # 클립보드에 복사하는 option
    if dist[num][num] == -1:
        dist[num][num] = dist[num][c] + 1
        q.append((num, num))
    
    # 화면에 클립보드 속 이모티콘을 붙여넣는 option
    if num + c <= s and dist[num + c][c] == -1:
        dist[num + c][c] = dist[num][c] + 1
        q.append((num + c, c))

    # 화면 속 이모티콘 1개를 지우는 option
    if num - 1 >= 0 and dist[num - 1][c] == -1:
        dist[num - 1][c] = dist[num][c] + 1
        q.append((num - 1, c))

# s개로 가는 이동 횟수들 중, 최소 이동 횟수 찾기
ans = 1e9
for i in range(s + 1):
    if dist[s][i] != -1:
        ans = min(ans, dist[s][i])

print(ans)

# 반례: 872 --> 22
# https://www.acmicpc.net/board/view/30100


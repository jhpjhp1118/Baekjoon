# https://www.acmicpc.net/problem/2250
import sys

"""
아이디어: 중위 순회를 한다.

주의) 노드번호가 오름차순으로 안 주어질 수 있다! (예제는 오름차순으로 주어져 있지만...)
"""

n = int(sys.stdin.readline().strip())

isRoots = [True]*n # root 노드가 무엇인지 찾기 위한 리스트. 어떤 노드의 자식 노드이면 False로 바꿔준다.
graph = [[] for _ in range(n + 1)]
for i in range(n):
    graph[i + 1] = list(map(int, sys.stdin.readline().strip().split()))

    # 자식 노드인 것은 False 로 바꿔준다.
    if graph[i + 1][1] != -1:
        isRoots[graph[i + 1][1] - 1] = False
    if graph[i + 1][2] != -1:
        isRoots[graph[i + 1][2] - 1] = False

# 노드 번호를 기준으로 정렬한다. graph[0] = [] 이므로, graph[1:] 를 정렬한다.
graph[1:] = sorted(graph[1:], key=lambda x: (x[0]))

# 끝까지 True 로 남은 노드를 root 노드로 간주한다. 인덱스르 맞추기 위해 1을 더한다.
root = isRoots.index(True) + 1

# 각 깊이에 대해, 존재하는 모든 노드의 열 정보(or 노드번호)를 기록할 리스트 생성
levels = [[] for _ in range(n + 1)]
# 각 노드번호에 해당하는 열 번호를 기록할 리스트 생성
cols = [-1] * (n + 1)
global idx
idx = 1


def inorder(node, level):
    global idx
    # 왼쪽 가지를 탐색한다.
    if graph[node][1] != -1:
        inorder(node=graph[node][1], level=level + 1)

    # (지금까지 나온 col번호) + 1 을 부모 노드의 열 위치로 잡는다.
    cols[node] = idx
    idx += 1 # idx 갱신한다.
    levels[level].append(node) # 현재 level에 해당 노드 번호를 추가한다.

    # 오른쪽 가지를 탐색한다.
    if graph[node][2] != -1:
        inorder(node=graph[node][2], level=level + 1)


inorder(node=root, level=1)

# 답으로 출력할 level, width 값 초기화하기
ans_level = -1
ans_width = -1

# 가장 너비가 넓은 레벨 & 그 너비값을 찾는다.
for lvl in range(1, n + 1):
    # 아무것도 없는 레벨이 나오면 탐색을 종료한다.
    if len(levels[lvl]) == 0:
        break
    # 각 레벨의 왼쪽 끝, 오른쪽 끝 열 번호 값을 얻는다.
    leftEnd = cols[levels[lvl][0]]
    rightEnd = cols[levels[lvl][-1]]

    # 너비 계산하기
    width = rightEnd - leftEnd + 1

    # 현재 ans_width보다 width가 더 클 경우, 그것으로 너비와 깊이를 갱신해준다.
    if ans_width < width:

        ans_width = width
        ans_level = lvl

print(ans_level, ans_width)

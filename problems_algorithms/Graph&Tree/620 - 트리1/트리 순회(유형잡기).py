# https://www.acmicpc.net/problem/1991
import sys

"""
전위 순회: dfs
중위 순회: 
"""
n = int(sys.stdin.readline().strip())

graph = []
for _ in range(n):
    graph.append(sys.stdin.readline().strip().split())
# 부모 노드의 알파벳 순서대로 graph 정렬하기
graph = sorted(graph, key=lambda x : (x[0]))

# 알파벳 A의 유니코드
unicodeA = ord("A")

# 출력할 답에 대한 리스트들 초기화하기
ans_pre = []
ans_in = []
ans_post = []

# 전위
def preorder(node):
    # 부모를 출력 답에 추가하기
    ans_pre.append(graph[node][0])  # 현재 노드의 알파벳을 추가한다.

    # 왼쪽 자식이 있으면 탐색
    if graph[node][1] != ".":
        preorder(ord(graph[node][1]) - unicodeA)

    # 오른쪽 자식이 있으면 탐색
    if graph[node][2] != ".":
        preorder(ord(graph[node][2]) - unicodeA)

# 중위
def inorder(node):
    # 왼쪽 자식이 있으면 탐색
    if graph[node][1] != ".":
        inorder(ord(graph[node][1]) - unicodeA)

    # 부모를 출력 답에 추가하기
    ans_in.append(graph[node][0])

    # 오른쪽 자식이 있으면 탐색
    if graph[node][2] != ".":
        inorder(ord(graph[node][2]) - unicodeA)

# 후위
def postorder(node):
    # 왼쪽 자식이 있으면 탐색
    if graph[node][1] != ".":
        postorder(ord(graph[node][1]) - unicodeA)

    # 오른쪽 자식이 있으면 탐색
    if graph[node][2] != ".":
        postorder(ord(graph[node][2]) - unicodeA)

    # 부모를 출력 답에 추가하기
    ans_post.append(graph[node][0])


preorder(0)
inorder(0)
postorder(0)

print(*ans_pre, sep="")
print(*ans_in, sep="")
print(*ans_post, sep="")


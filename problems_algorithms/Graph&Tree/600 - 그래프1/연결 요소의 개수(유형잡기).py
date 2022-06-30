# https://www.acmicpc.net/problem/11724
import sys

# 가정: 연결된 노드 중 더 작은 번호의 노드가, 부모 노드가 된다.
# root 노드: 한 그래프 집합의 가장 작은 번호의 노드. 가장 시초의 부모 노드
# 현재의 union된 그래프 상태에서, 주어진 node의 root 노드를 찾는 함수
def find_parent(parent, node):

    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

# 링크로 연결된 두 노드를 하나의 그래프 집합으로 엮어준다. 이 때, 부모-자식 관계도 정해준다.
def union_parent(parent, n1, n2):
    parent1 = find_parent(parent, n1)
    parent2 = find_parent(parent, n2)

    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2

n, m = list(map(int, sys.stdin.readline().strip().split()))

parent = [i for i in range(n+1)] # 자기 노드 번호로 root 노드 초기화

# 연결되는 노드끼리 집합으로 묶어나간다.
for i in range(m):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))
    union_parent(parent, p1, p2)

# 모든 노드에 대해, root 노드를 찾아준다.
for i in range(n+1):
    find_parent(parent, i)

# 중복 요소를 1개로 줄이고, parent의 dummy 값인 0(=parent[0]) 을 제외하고 개수를 센다.
print(len(set(parent)) - 1)




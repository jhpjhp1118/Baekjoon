# https://www.acmicpc.net/problem/11724
import sys

def find_parent(parent, node):

    if parent[node] != node:
        find_parent(parent, parent[node])
    return node

def union_parent(parent, n1, n2):
    parent1 = find_parent(parent, n1)
    parent2 = find_parent(parent, n2)

    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2

n, m = list(map(int, sys.stdin.readline().strip().split()))

parent = [i for i in range(n+1)] # 자기 노드 번호로 root 노드 초기화


#
for i in range(m):
    p1, p2 = list(map(int, sys.stdin.readline().strip().split()))







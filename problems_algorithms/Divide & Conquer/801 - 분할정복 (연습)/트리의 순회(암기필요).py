# https://www.acmicpc.net/problem/2263
import sys

"""
참고: https://ku-hug.tistory.com/135?category=978336
아이디어: 
    1. 각 서브 트리의 root 노드(가장 위에 위치한 노드)는 postorder의 마지막에 오는 값이다. (= preorder에 추가될 값)
    2. inorder & postorder에서 각각 root 노드 기준, 왼쪽에 있는 서브트리 & 오른쪽에 있는 서브트리를 그룹으로 구분할 수 있다.
        (inorder에서 구분지은 서브트리와, postorder에서 구분지은 서브트리는, 각각 같은 성분을 가진다. 
            <-- 같은 서브트리를 표현하는 것이므로 당연하다!)
    3. root 노드를 기준으로, 왼쪽에 있는 서브 트리 & 오른쪽에 있는 서브트리를 각각 inorder & postorder로 표현해주면, 
        - 1번 규칙을 통해 해당 서브트리의 root 노드를 preorder 값으로 추가하면 된다.
"""

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().strip().split()))
postorder = list(map(int, input().strip().split()))

# inorder에서의 성분별 index 기록하기
nodeNum = [0]*(n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    # 서브트리의 마지막 노드까지 다 탐색했으면, 재귀호출을 그만한다.
    if (inStart > inEnd) or (postStart > postEnd):
        return

    # 해당 서브트리의 root 노드값을 얻고, 출력한다.
    root = postorder[postEnd]
    print(root, end=" ")

    # root 노드 기준으로, 왼쪽 서브트리의 노드 개수 & 오른쪽 서브트리의 노드 개수를 구한다.
    leftNode = nodeNum[root] - inStart
    rightNode = inEnd - nodeNum[root]

    # 왼쪽 & 오른쪽 서브트리에 대해서 재귀호출한다.
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, n - 1, 0, n - 1)



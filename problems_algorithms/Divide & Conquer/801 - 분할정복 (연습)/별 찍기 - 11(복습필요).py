# https://www.acmicpc.net/problem/2448
import sys

input = sys.stdin.readline
n = int(input().strip())

def appendRow(len):
    # 현재 깊이의 기준 row 개수가 3개일 경우, 정해진 삼각형 문양을 반환한다.
    if len == 3:
        L = ["  *  ",
             " * * ",
             "*****"]
        return L

    stars = appendRow(len//2)
    L = []

    # 위쪽 삼각형 1개
    for s in stars:
        # 양쪽에 동일한 길이의 여백을 추가해준다.
        L.append((len//2)*" " + s + (len//2)*" ")

    # 아래쪽 삼각형 2개
    for s in stars:
        # 2개의 삼각형 사이에 1 칸의 여백을 추가해준다.
        L.append(s + " " + s)

    return L


L = appendRow(n)
print("\n".join(L))

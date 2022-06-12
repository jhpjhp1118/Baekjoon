# https://www.acmicpc.net/problem/11723
import sys

m = int(sys.stdin.readline().strip())
# (0번째 성분은 무시) 1~20을 가지고 있는지 여부를 표시한다. (가지고 있으면 1, 없으면 0)
s = [0]*21


for _ in range(m):
    arr = sys.stdin.readline().strip().split()

    if arr[0] == "all":
        s = [1]*21
    elif arr[0] == "empty":
        s = [0] * 21
    elif arr[0] == "add":
        s[int(arr[1])] = 1
    elif arr[0] == "remove":
        s[int(arr[1])] = 0
    elif arr[0] == "check":
        print(s[int(arr[1])])
    elif arr[0] == "toggle":
        s[int(arr[1])] ^= 1
    else:
        # 걍 내맘대로 만듦;;
        print("Error!")
        break


# https://www.acmicpc.net/problem/10809
import sys

line = sys.stdin.readline().strip()

num_alpha = [-1]*26
a_ascii = ord("a")
for i, char in enumerate(line):
    # 해당 문자의 num_alpha 값이 -1 일 때, i를 값으로 채워넣는다.
    if num_alpha[ord(char) - a_ascii] == -1:
        num_alpha[ord(char) - a_ascii] = i

print(*num_alpha)

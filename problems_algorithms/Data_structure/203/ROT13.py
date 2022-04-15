# https://www.acmicpc.net/problem/11655
import sys

line = sys.stdin.readline().rstrip("\n")

result = ""
for char in line:
    if char.isnumeric() or char.isspace():
        result += char
    else:
        # 대문자/소문자에 따라, 첫 알파벳의 아스키 코드 체크하기
        if char.isupper():
            ascii_a = ord("A")
        elif char.islower():
            ascii_a = ord("a")

        # (char의 아스키 코드 - ascii_A + 13) 이 26 보다 크면, chr(ascii_A + (그 넘는 만큼)) --> 나머지로 구현
        ascii_rot = (ord(char) - ascii_a + 13) % 26
        result += chr(ascii_a + ascii_rot)
print(result)

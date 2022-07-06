# https://www.acmicpc.net/problem/1339
import sys

"""
아이디어: [그리디 알고리즘]
        알파벳별로 해당되는 단위값의 합을 기록한다.
        알파벳이 무엇인지는 관심없고, 그 단위값의 합이 제일 큰 것부터 9, 8, 7 ... 를 곱해서 합해가면 된다.
ex)
2
GCF
ACDEB
단위값: [('A', 10000), ('B', 1), ('C', 1010), ('D', 100), ('E', 10), ('F', 1), ('G', 100)]

        
참고 링크: https://hongcoding.tistory.com/76

"""

n = int(sys.stdin.readline().strip())

words = []
for i in range(n):
    words.append(list(sys.stdin.readline().strip()))

alphaDict = {} # 알파벳별로 해당되는 단위값의 합을 기록하기 위한 딕셔너리 생성하기

# 모든 단어에 대해
for word in words:
    # 각 글자마다
    for i in range(len(word)):
        # 만약 alphaDict에 이미 해당 알파벳이 있을 경우
        if word[i] in alphaDict:
            # 대응하는 단위값을 더해준다.
            alphaDict[word[i]] += 10**(len(word) - i - 1)
        # alphaDict에 없는 알파벳일 경우
        else:
            # 해당 알파벳에 대응하는 단위값을 생성한다.
            alphaDict[word[i]] = 10**(len(word) - i - 1)

# alphaDict의 value들만 뽑아낸 뒤, 내림차순으로 정렬한다.
vals = [val for val in alphaDict.values()]
vals = sorted(vals, reverse=True)

# 단위값이 큰 것부터, 9 부터 차례로 곱해서 더해간다.
ans = 0
num = 9
for val in vals:
    ans += val * num
    num -= 1

print(ans)




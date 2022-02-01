# https://codeup.kr/problem.php?id=6064
a, b, c = map(int, input().split())
compareAB = (a if a <= b else b) # a 와 b를 비교하여 더 작은 것을 찾아낸다
compareC = (compareAB if compareAB <= c else c) # 그것을 c와 비교하여 더 작은 것을 찾아낸다
print(compareC)

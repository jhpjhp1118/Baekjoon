# problem 2884
h, m = map(int, input().split())

# m - 45가 0보다 작으면, 60 - m 을 표시할 것이다.
#           0보다 크면, m - 45 를 표시할 것이다. 그리고 h를 1 만큼 뺀다
if m - 45 < 0:
    finalM = 15 + m
    h -= 1
else:
    finalM = m - 45

# h 가 0보다 작으면, 24 - h 를 표시할 것이다.
#     0보다 크면, h 를 표시할 것이다.
if h < 0:
    finalH = h + 24
else:
    finalH = h

print(finalH, finalM, sep=" ")
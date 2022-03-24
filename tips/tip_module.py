# collections.Counter 사용
from collections import Counter

colors = Counter(['blue', 'green', 'red', 'blue','red','blue'])

print(colors)
# Counter({'blue': 3, 'red': 2, 'green': 1})

print(colors.most_common())
# [('blue', 3), ('red', 2), ('green', 1)]

print(colors.most_common(2))
# 가장 많은 것 부터 2개 출력
# [('blue', 3), ('red', 2)]
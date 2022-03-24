# https://www.acmicpc.net/problem/2108
n = int(input())

# Get number inputs
num = []
for _ in range(n):
    num.append(int(input()))

num = sorted(num)
# mean value
mean = round(sum(num)/n)

# mid value
mid = num[n//2]

# most frequently seen value
counts = {} # Key: 나타나는 횟수, Value: 해당 횟수만큼 나타나는 값
for i in range(1, n+1):
    counts[i] = []

maxCount = 1
count = 1
for j in range(1, n): # n-1 번만큼 반복
    if num[j] == num[j-1]:
        count += 1
    else: # 마지막 성분이 아니고, 새로운 성분이 나왔을 때
        counts[count].append(num[j-1])
        if maxCount < count: maxCount = count
        count = 1

    if j == n - 1: # 마지막 성분일 때
        counts[count].append(num[j])
        if maxCount < count: maxCount = count

if n == 1:
    counts[1].append(num[0])

counts[maxCount].sort()
if len(counts[maxCount]) == 1:
    most = counts[maxCount][0]
else:
    most = counts[maxCount][1]

# r = max - min
r = num[-1] - num[0]

print(mean, mid, most, r, sep="\n")

# 예시 인풋
# 5
# -1
# -2
# -3
# -1
# -2


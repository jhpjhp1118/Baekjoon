########### Input: 123 456 --> Output: 123 456 (Integer의 형태로)
a, b = map(int, input().split())

print(a, b)

########### Input: 123 456 --> Output: [123, 456]
a = list(map(int, input().split()))

print(a)

########### Input: 123 --> Output: [1, 2, 3]
a = list(map(int, list(input())))

print(a)

########### Input:
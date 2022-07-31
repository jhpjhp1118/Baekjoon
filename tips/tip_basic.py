########### Input: 123 456 --> Output: 123 456 (Integer의 형태로)
a, b = map(int, input().split())

print(a, b)

########### Input: 123 456 --> Output: [123, 456]
a = list(map(int, input().split()))

print(a)

########### Input: 123 --> Output: [1, 2, 3]
a = list(map(int, list(input())))

print(a)

########### Input: A --> Output: 65
n = ord(input()) #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.

print(n)

########### Input: love 3 --> Output: lovelovelove
w, n = input().split()

print(w * int(n))

########### Input: 3.141592 --> Output: 3.14
a = float(input())

print( format(a, ".2f") ) # (소수점 3번째 자리에서 반올림한) 소수점 2번째 자리까지의 값을 출력해준다.

########### Input: 0 --> Output: True
########### Input: 0이 아닌 값 --> Output: False
n = int(input())
print(bool(n))

########## Input: 0 --> Output: False
a = bool(int(input()))
print(not a) # boolean T/F 맞바꾸기


########## Output: 10 9 8 7 6 5 4 3 2 1
start = 10
stop = 0
step = -1
for i in range(start, stop, step)
    print(i, end=" ")

########## Output: 1 (Smallest positive value in list "l")
l = [-1, -2, 1, 5, 2]
val = min([i for i in l if i > 0])
print(val)

########## Output: 2 (Index of smallest positive value in list "l")
l = [-1, -2, 1, 5, 2]
val = l.index(min([i for i in l if i > 0]))
print(val)

########## input 0 & 1 --> Output: 1 & 0 (비트연산자)
a = 1
a ^= 1 # a: 0
a ^= 1 # a: 1

# 숫자로 된 리스트를 여백없이 출력하는 명령어
row = [1, 2, 3]
print("".join(list(map(str, row))))

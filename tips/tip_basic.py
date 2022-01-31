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

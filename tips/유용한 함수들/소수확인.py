def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1): # num = 2, 3 일 때는 loop가 하나도 돌지 않아서 True가 리턴됨.
        if num % i == 0:
            return False
    return True


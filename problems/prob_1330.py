# problem 1330
a, b = map(int, input().split())

if a >= b :
    if a - b < 1:
        print("==")
    else:
        print(">")

else:
    print("<")

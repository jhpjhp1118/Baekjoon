# https://codeup.kr/problem.php?id=6082
s = input()

for i in range(1, int(s) + 1):

    iList = list(str(i))
    sum = iList.count("3") + iList.count("6") + iList.count("9")
    if sum == 0:
        print(i)
    else:
        print("X"*sum)
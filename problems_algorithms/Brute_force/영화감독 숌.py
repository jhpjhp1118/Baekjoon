# https://www.acmicpc.net/problem/1436
import sys
n = int(sys.stdin.readline().strip())

i = 1
final_countdown = 0 # When "i" has 666, increase it
while True:
    nums = list(map(int, list(str(i))))
    count = 0
    max_count = 0
    for j in range(0, len(nums) - 1):
        if (nums[j] == nums[j+1]) and (nums[j] == 6):
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count

    if max_count >= 2:
        final_countdown += 1

    if final_countdown == n:
        print(i)
        break
    i += 1

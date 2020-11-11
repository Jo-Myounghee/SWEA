import sys
n, x = map(int, sys.stdin.readline().split())
nums = list(sys.stdin.readline().split())
for i in range(n):
    if int(nums[i]) < x:
        print(nums[i], end=" ")
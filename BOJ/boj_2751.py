import sys


N = int(input())
nums = [(sys.stdin.readline().strip()) for _ in range(N)]
nums.sort()
print(*nums, sep="\n")
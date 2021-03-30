import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1] * N

stack.append(0)
i = 1

while stack and i < N:
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack[-1]] = nums[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*answer)
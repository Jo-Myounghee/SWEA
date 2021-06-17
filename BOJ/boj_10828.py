from collections import deque
import sys


def program(order):
    global stack
    if len(order) == 2:
        stack.append(int(order[1]))
    else:
        if order[0] == 'pop':
            print(-1) if len(stack) == 0 else print(stack.pop())
        elif order[0] == 'size':
            print(len(stack))
        elif order[0] == 'empty':
            print(1) if len(stack) == 0 else print(0)
        elif order[0] == 'top':
            print(-1) if len(stack) == 0 else print(stack[-1])


N = int(input())
stack = deque()
for _ in range(N):
    program(sys.stdin.readline().split())
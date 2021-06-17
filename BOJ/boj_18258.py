from collections import deque
import sys


def program(order):
    global q
    if len(order) == 2:
        q.append(order[1])
    elif order[0] == 'pop':
        print(-1) if len(q) == 0 else print(q.popleft())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif order[0] == 'front':
        print(-1) if len(q) == 0 else print(q[0])
    elif order[0] == 'back':
        print(-1) if len(q) == 0 else print(q[-1])


N = int(input())
q = deque()
for _ in range(N):
    program(sys.stdin.readline().split())
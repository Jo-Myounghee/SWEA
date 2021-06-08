'''
10
7 6
9
1 2
1 3
1 4
9 1
9 10
3 5
3 6
2 7
2 8
-> 4

5
1 5
4
1 2
1 3
2 4
3 5
-> 2
'''
from collections import deque

N = int(input())
S, G = map(int, input().split())
M = int(input())
connections = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    connections[x].append(y)
    connections[y].append(x)

visited = [False] * (N+1)
is_answer = False
q = deque()
q.append((S, 0))

while q:
    now, cnt = q.popleft()
    if now == G:
        is_answer = True
        print(cnt)
        break
    else:
        if not visited[now]:
            for _next in connections[now]:
                q.append((_next, cnt+1))
            visited[now] = True

if not is_answer:
    print(-1)


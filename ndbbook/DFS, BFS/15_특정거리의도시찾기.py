# BFS

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    s, f = map(int, input().split())
    graph[s].append(f)

visited = [-1] * (n+1)
visited[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if visited[next_node] == -1:
            visited[next_node] = visited[now] + 1
            q.append(next_node)

check = False

for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
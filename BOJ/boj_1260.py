import sys
from collections import deque

def dfs(v):
    global graph
    visited_dfs[v] = True
    dfs_ans.append(v)
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    global graph
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        bfs_ans.append(v)
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


N, M, V = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    s, g = map(int, sys.stdin.readline().strip().split())
    graph[s].append(g)
    graph[g].append(s)

for i in range(N):
    graph[i].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs_ans = []
bfs_ans = []

dfs(V)
bfs(V)

print(*dfs_ans)
print(*bfs_ans)
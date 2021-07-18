def dfs(i, cnt):
    if cnt == 5:
        print(1)
        exit()
    for v in graph[i]:
        if not visited[v]:
            visited[v] = True
            dfs(v, cnt + 1)
            visited[v] = False


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

for i in range(N):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(0)
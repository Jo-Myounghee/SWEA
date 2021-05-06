from collections import deque

def bfs(n):
    global visited, path
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            p = []
            while x != N:
                p.append(x)
                x = path[x]
            p.append(n)
            p.reverse()
            print(*p)
            return
        for nx in (x*2, x+1, x-1):
            if 0 <= nx <= MAX and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1
                path[nx] = x
MAX = 100000
N, K = map(int, input().split())
visited = [-1] * (MAX+1)
path = [0] * (MAX+1)
bfs(N)
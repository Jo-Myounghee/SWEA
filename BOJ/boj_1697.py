from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == K:
            print(visited[K])
            return
        for nx in (x*2, x+1, x-1):
            if 0 <= nx <= MAX:
                if visited[nx] == -1 or visited[nx] > visited[x] + 1:
                    q.append(nx)
                    visited[nx] = visited[x] + 1

MAX = 100000
N, K = map(int, input().split())
visited = [-1] * (MAX+1)
bfs(N)
from collections import deque


def bfs():
    global F, S, G, U, D, visited
    visited = [False] * 1000001
    q = deque()
    visited[S] = True
    q.append((S, 0))

    while q:
        now, cnt = q.popleft()
        if now == G:
            return cnt
        if now + U <= F and not visited[now+U]:
            q.append((now+U, cnt+1))
            visited[now+U] = True
        if now - D >= 1 and not visited[now-D]:
            q.append((now-D, cnt+1))
            visited[now-D] = True
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
print(bfs())


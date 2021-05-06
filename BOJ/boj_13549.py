'''
1 2
-> 0

0 0
-> 0

5 5
-> 0
100000 0
-> 100000
25000 100000
-> 0

2 1024
-> 0
99999 100000
-> 1
'''
from collections import deque

def bfs(N):
    global dist
    q = deque()
    q.append(N)
    dist[N] = 0
    while q:
        x = q.pop()
        if x == K:
            print(dist[K])
            return
        for nx in (x*2, x-1, x+1):
            if 0 <= nx <= MAX and dist[nx] == -1:
                if nx == x*2:
                    q.append(nx)
                    dist[nx] = dist[x]
                else:
                    q.appendleft(nx)
                    dist[nx] = dist[x] + 1

MAX = 100000
N, K = map(int, input().split())
dist = [-1] * (MAX+1)
bfs(N)
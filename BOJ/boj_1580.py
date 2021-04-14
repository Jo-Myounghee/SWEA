from collections import deque

def isWall(x, y):
    if x < 0 or y < 0 or x >= M or y >= N or board[y][x] == 'X':
        return True
    return False

def bfs():
    global _ax, _ay, _bx, _by, goalA, goalB
    while q:
        ax, ay, bx, by, c = q.popleft()
        if ax == _bx and ay == _by and bx == _ax and by == _ay:
            print(c)
            return

        for i in range(9):
            nax = ax + dx[i]
            nay = ay + dy[i]
            if isWall(nax, nay):
                continue

            for j in range(9):
                nbx = bx + dx[j]
                nby = by + dy[j]
                if isWall(nbx, nby):
                    continue

                if visited[nay][nax][nby][nbx]:
                    continue

                if nax == nbx and nay == nby:
                    continue

                if nax == bx and nay == by and nbx == ax and nby == ay:
                    continue

                if not visited[nay][nax][nby][nbx]:
                    q.append((nax, nay, nbx, nby, c+1))
                    visited[nay][nax][nby][nbx] = True
    print(-1)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = (0, 1, 1, 1, 0, -1, -1, -1, 0), (-1, -1, 0, 1, 1, 1, 0, -1, 0)

for y in range(N):
    for x in range(M):
        if board[y][x] == 'A':
            _ax, _ay = x, y
        elif board[y][x] == 'B':
            _bx, _by = x, y

q = deque()
q.append((_ax, _ay, _bx, _by, 0))
visited[_ay][_ax][_by][_bx] = True
bfs()
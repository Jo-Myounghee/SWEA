from collections import deque

def move(_x, _y, _dx, _dy, _c):
    while board[_y+_dy][_x+_dx] != '#' and board[_y][_x] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    while q:
        rx, ry, bx, by, c = q.popleft()

        if c > 10:
            break
        for i in range(4):
            nrx, nry, nrc = move(rx, ry, dx[i], dy[i], c)
            nbx, nby, nbc = move(bx, by, dx[i], dy[i], c)

            # 만약 파란색이 골에 빠졌다면 -> 무시
            if board[nby][nbx] == 'O':
                continue
            # 만약 빨간색이 골에 빠졌다면 -> cnt 출력하고 return
            if board[nry][nrx] == 'O':
                print(c)
                return
            # 만약 빨간색과 파란색이 같은 위치라면
            if nrx == nbx and nry == nby:
                if nrc > nbc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 만약 방문하지 않은 곳이라면
            if not visited[nry][nrx][nby][nbx]:
                q.append((nrx, nry, nbx, nby, c+1))
                visited[nry][nrx][nby][nbx] = True
    print(-1)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            _rx, _ry = x, y
        elif board[y][x] == 'B':
            _bx, _by = x, y

q = deque()
q.append((_rx, _ry, _bx, _by, 1))
visited[_ry][_rx][_by][_bx] = True

bfs()
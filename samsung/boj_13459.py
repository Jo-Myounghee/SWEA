from collections import deque

def move(_x, _y, _dx, _dy, _c):
    while board[_y + _dy][_x + _dx] != '#' and board[_y][_x] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                print(1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx[i], nby - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not check[nry][nrx][nby][nbx]:
                check[nry][nrx][nby][nbx] = True
                q.append((nrx, nry, nbx, nby, d + 1))
    print(0)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
check = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

_rx, _ry, _bx, _by = [0] * 4
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            _rx, _ry = x, y
        elif board[y][x] == 'B':
            _bx, _by = x, y

q.append((_rx, _ry, _bx, _by, 0))
check[_ry][_rx][_by][_bx] = True

bfs()
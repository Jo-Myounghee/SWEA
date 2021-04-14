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
            # 파란 공이 구멍에 빠졌을 때 -> 무시
            if board[nby][nbx] == 'O':
                continue
            # 빨간 공이 구멍에 빠졌을 때 -> 종료
            if board[nry][nrx] == 'O':
                print(1)
                return
            # 만약 빨간 공과 파란 공의 위치가 같다면
            if nrx == nbx and nry == nby:
                # 카운트를 비교한다(1): 파란색이 더 먼저 도착했음 -> 빨간색이 온만큼 한 번 물러선다.
                if rc > bc:
                    nrx, nry = nrx - dx[i], nby - dy[i]
                # 카운트를 비교한다(2): 빨간색이 더 먼저 도착했음 -> 파란색이 온만큼 한 번 물러선다.
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            # 만약 방문하지 않은 곳이라면
            if not check[nry][nrx][nby][nbx]:
                # 방문 체크하고
                check[nry][nrx][nby][nbx] = True
                # 다시 BFS
                q.append((nrx, nry, nbx, nby, d + 1))
    print(0)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
check = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# 좌 하 우 상
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

_rx, _ry, _bx, _by = [0] * 4
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            _rx, _ry = x, y
        elif board[y][x] == 'B':
            _bx, _by = x, y

# 초기 상태 append
q.append((_rx, _ry, _bx, _by, 0))
# 초기 visit 체크
check[_ry][_rx][_by][_bx] = True

bfs()
def is_board(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def order(d, s):
    global clouds, board

    def create_clouds():
        for y in range(N):
            for x in range(N):
                if board[y][x] >= 2 and not visited[y][x]:
                    clouds.append((x, y))
                    board[y][x] -= 2
    new = []
    visited = [[False] * N for _ in range(N)]
    for cx, cy in clouds:
        nx, ny = (cx + (dx[d] * s))%N, (cy + (dy[d] * s))%N
        while nx < 0:
            nx += N
        while ny < 0:
            ny += N
        board[ny][nx] += 1
        visited[ny][nx] = True
        new.append((nx, ny))

    clouds = []
    _dx = (-1, -1, +1, +1)
    _dy = (-1, +1, -1, +1)
    for i in range(len(new)):
        _nx, _ny = new[i][0], new[i][1]
        add_water = 0
        for k in range(4):
            tx = _nx + _dx[k]
            ty = _ny + _dy[k]
            if is_board(tx, ty) and board[ty][tx] > 0:
                add_water += 1
        board[_ny][_nx] += add_water
    create_clouds()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
inputs = [list(map(int, input().split())) for _ in range(M)]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

clouds = [(0, N-2), (1, N-2), (0, N-1), (1, N-1)]
for i in range(M):
    d, s = inputs[i][0], inputs[i][1]
    order(d, s)

answer = 0
for i in range(N):
    answer += sum(board[i])
print(answer)
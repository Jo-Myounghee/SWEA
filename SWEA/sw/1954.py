def main(tc):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    n_val = 1
    nx, ny = 0, 0
    _d = 0

    def can_write(x, y):
        if 0 <= x < N and 0 <= y < N and board[y][x] == 0:
            return True
        return False

    def write(x, y, val, d):
        if val > N*N:
            return

        board[y][x] = val
        tx, ty = x + dx[d], y + dy[d]
        if can_write(tx, ty):
            write(tx, ty, val+1, d)
        else:
            tx, ty = x + dx[(d+1)%4], y + dy[(d+1)%4]
            if can_write(tx, ty):
                write(tx, ty, val+1, (d+1)%4)

    write(nx, ny, n_val, _d)
    print('#{}'.format(tc))
    for i in range(N):
        print(*board[i])

T = int(input())
for tc in range(1, T+1):
    main(tc)

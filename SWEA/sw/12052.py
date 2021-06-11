def fix():
    global board
    nx, ny = 0, 0

    def start_location(x, y):
        if board[y][x] == '#':
            return x, y
        else:
            for _x in range(M-x):
                if board[y][x+_x] == '#':
                    return x + _x, y
            for _y in range(N-y):
                for _x in range(M):
                    if board[y+_y][x+_x] == '#':
                        return x + _x, y + _y

    def break_cnt():
        cnt = 0
        for y in range(N):
            for x in range(M):
                if board[y][x] == '#':
                    cnt += 1
        return cnt

    def fix_tile(x, y):
        dx = (0, 1, 0, 1)
        dy = (0, 0, 1, 1)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < M and 0 <= ty < N and board[ty][tx] == '#':
                board[ty][tx] = '.'
            else:
                return False
        return True

    _cnt = break_cnt()
    while _cnt > 0 and _cnt % 4 == 0:
        sx, sy = start_location(nx, ny)
        if not fix_tile(sx, sy):
            return False
        _cnt = break_cnt()
    if break_cnt() == 0:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    answer = 'NO' if not fix() else 'YES'
    print('#{} {}'.format(tc, answer))
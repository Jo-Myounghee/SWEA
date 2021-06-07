from collections import deque


def rotate_board(r):
    global N, M, board
    q = deque()
    _width, _height = M, N
    time = min(_width, _height) // 2
    nx, ny = 0, 0

    while time >= 1:
        for i in range(_width-1):
            q.append(board[ny][nx+i])
        for i in range(_height-1):
            q.append(board[ny+i][nx+_width-1])
        for i in range(_width-1):
            q.append(board[ny+_height-1][nx+_width-1-i])
        for i in range(_height-1):
            q.append(board[ny+_height-1-i][nx])

        q.rotate(-r)

        for i in range(_width-1):
            board[ny][nx+i] = q.popleft()
        for i in range(_height-1):
            board[ny+i][nx+_width-1] = q.popleft()
        for i in range(_width-1):
            board[ny+_height-1][nx+_width-1-i] = q.popleft()
        for i in range(_height-1):
            board[ny+_height-1-i][nx] = q.popleft()

        _width -= 2
        _height -= 2
        nx += 1
        ny += 1
        time = min(_width, _height) // 2


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotate_board(R)
for i in range(N):
    print(*board[i])
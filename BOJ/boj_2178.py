from collections import deque

def is_road(x, y):
    global N, M
    if 0 <= x < M and 0 <= y < N:
        return True
    return False


def find_exit(ix, iy, i_cnt):
    global board
    q = deque()
    q.append((ix, iy, i_cnt))

    _dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (M-1, N-1):
            return cnt
        for i in range(4):
            _x, _y = x + _dir[i][0], y + _dir[i][1]
            if is_road(_x, _y) and board[_y][_x] == 1:
                q.append((_x, _y, cnt+1))
                board[_y][_x] = 0


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
print(find_exit(0, 0, 1))
from collections import deque


def find_group(nx, ny):
    if is_board(nx, ny) and not visited[ny][nx]:
        visited[ny][nx] = True
        if board[ny][nx] == 2:
            for i in range(4):
                tx, ty = nx + dx[i], ny + dy[i]
                if is_board(tx, ty) and not visited[ty][tx]:
                    find_group(tx, ty)
    return


def comb(item, s, cnt):
    global answer
    if cnt == 2:
        answer = max(put_stone(item), answer)
        return
    for i in range(s, len(bin_lst)):
        comb(item+[bin_lst[i]], i+1, cnt+1)


def is_board(x, y):
    if 0 <= x < M and 0 <= y < N:
        return True
    return False


def put_stone(locations):
    _visited = [[False] * M for _ in range(N)]
    stones = 0

    def is_around(sx, sy):
        _cnt = 1 # 둘러쌓인 상대 돌의 갯수
        q = deque()
        q.append((sx, sy))
        _visited[sy][sx] = True

        while q:
            nx, ny = q.popleft()
            for i in range(4):
                tx, ty = nx + dx[i], ny + dy[i]
                if is_board(tx, ty) and not _visited[ty][tx]:
                    if temp_board[ty][tx] == 2:
                        _cnt += 1
                        _visited[ty][tx] = True
                        q.append((tx, ty))
                    elif temp_board[ty][tx] == 0 and temp_board[ny][nx] == 2:
                        return 0
        return _cnt

    temp_board = [board[i][:] for i in range(N)]
    for lx, ly in locations:
        temp_board[ly][lx] = 1
    # 둘러 쌓였는지 확인
    for _rx, _ry in robots:
        if not _visited[_ry][_rx]:
            _stone = is_around(_rx, _ry)
            stones += _stone
    return stones


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
bin_lst = []
robots = []
answer = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            bin_lst.append((x, y))
        elif board[y][x] == 2 and not visited[y][x]:
            robots.append((x, y))
            find_group(x, y)

comb([], 0, 0)
print(answer)
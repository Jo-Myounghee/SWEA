from collections import deque

def isBoard(x, y):
    if 0 <= x < W and 0 <= y < H:
        return True
    return False


def downBoard(cnt):
    for x in range(W):
        temp_row = []
        for y in range(H - 1, -1, -1):
            if board[y][x] > 0:
                temp_row.append(board[y][x])
        for y in range(H - 1, -1, -1):
            if temp_row:
                val = temp_row.pop(0)
                board[y][x] = val
            else:
                board[y][x] = 0
    solve(cnt + 1)

def bomb(x, y, cnt):
    q = deque()
    q.append((x, y))
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))

    visited = [[False] * W for _ in range(H)]
    visited[y][x] = True
    while q:
        nx, ny = q.popleft()
        size = board[ny][nx]
        board[ny][nx] = 0

        if size > 0:
            for i in range(1, size):
                for j in range(4):
                    tx, ty = nx + dir[j][0] * i, ny + dir[j][1] * i
                    if isBoard(tx, ty) and not visited[ty][tx] and board[ty][tx] != 0:
                        visited[ty][tx] = True
                        q.append((tx, ty))
    downBoard(cnt)

def findBomb(x, cnt):
    global board
    y = 0
    while y < H and board[y][x] == 0:
        y += 1
    if y <= H - 1:
        temp_board = [board[i][:] for i in range(len(board))]
        bomb(x, y, cnt)
        board = [temp_board[i][:] for i in range(len(temp_board))]
    return

def countBomb():
    cnt = 0
    for y in range(H):
        for x in range(W):
            if board[y][x] > 0:
                cnt += 1
    return cnt

def solve(cnt):
    global minAns

    count_bomb = countBomb()

    if count_bomb == 0:
        minAns = 0
        return

    if cnt == N:
        minAns = min(minAns, count_bomb)
        return

    for i in range(W):
        findBomb(i, cnt)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    minAns = W * H

    solve(0)
    print('#{} {}'.format(tc, minAns))
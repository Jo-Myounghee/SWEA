def isWall(x, y):
    if x < 0 or x >= C or y < 0 or y >= R or board[y][x]:
        return True
    return False

C, R = map(int, input().split())
K = int(input())
board = [[0]*C for _ in range(R)]
if K > (C*R):
    print(0)
else:
    cx, cy = 0, 0
    dir = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 1
    board[cy][cx] = 1
    while cnt < K:
        tx = cx + dx[dir]
        ty = cy + dy[dir]
        if isWall(tx, ty):
            dir = (dir+1) % 4
            cx += dx[dir]
            cy += dy[dir]
        else:
            cx, cy = tx, ty
        board[cy][cx] = 1
        cnt += 1
    print(cx+1, cy+1)

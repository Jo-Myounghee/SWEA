def game():
    global board, walls
    now_pos = [[0, 7]]

    def is_wall(x, y):
        if x < 0 or x >= 8 or y < 0 or y >= 8 or board[y][x] == '#':
            return True
        return False

    def move_walls():
        new_walls = []
        new_board = [['.']*8 for _ in range(8)]
        for i in range(len(walls)):
            wx, wy = walls[i][0], walls[i][1]
            if wy + 1 == 8:
                continue
            else:
                new_walls.append((wx, wy+1))
                new_board[wy+1][wx] = '#'
                board[wy+1][wx] = '#'
        return new_walls, new_board

    def go_move(now):
        _dx = (0, 1, 1, 1, 0, -1, -1, -1, 0)
        _dy = (-1, -1, 0, 1, 1, 1, 0, -1, 0)

        new_pos = []
        for nx, ny in now:
            for i in range(9):
                tx, ty = nx + _dx[i], ny + _dy[i]
                if not is_wall(tx, ty):
                    new_pos.append((tx, ty))
        return new_pos

    while walls:
        walls, temp_board = move_walls()
        now_pos = go_move(now_pos)
        if not now_pos:
            return False
        board = temp_board
    return True


board = [list(input()) for _ in range(8)]
walls = []
for y in range(8):
    for x in range(8):
        if board[y][x] == '#':
            walls.append((x, y))
print(int(game()))

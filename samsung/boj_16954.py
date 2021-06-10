'''
........
........
........
........
........
#.......
.#......
.#......
-> 1

..###.##
##...#.#
..#.#..#
#.#...#.
.#...#.#
.#.#..##
#..#..#.
..#....#
-> 1
'''
def game(walls):
    global board
    nows = [[0, 7]]

    def is_wall(x, y):
        if x < 0 or x >= 8 or y < 0 or y >= 8 or board[y][x] == '#' or new_board[y][x] == '#':
            return True
        return False

    def wall_move(walls):
        new_walls = []
        wall_board = [['.']*8 for _ in range(8)]
        for i in range(len(walls)):
            wx, wy = walls[i][0], walls[i][1]
            if wy + 1 == 8:
                continue
            else:
                new_walls.append((wx, wy+1))
                wall_board[wy+1][wx] = '#'
        return new_walls, wall_board

    def move(nx, ny):
        lst = []
        dx = (0, 1, 1, 1, 0, -1, -1, -1, 0)
        dy = (-1, -1, 0, 1, 1, 1, 0, -1, 0)
        for i in range(9):
            tx, ty = nx + dx[i], ny + dy[i]
            if not is_wall(tx, ty):
                if (tx, ty) == (7, 0):
                    return 'goal'
                lst.append((tx, ty))
        return lst

    while walls:
        walls, new_board = wall_move(walls)
        new_nows = []
        for nx, ny in nows:
            move_result = move(nx, ny)
            if move_result == 'goal':
                return True
            elif len(move_result) == 0:
                return False
            else:
                new_nows += move(nx, ny)
        nows = new_nows
        board = new_board
    return True


board = [list(input()) for _ in range(8)]
walls_lst = [] # 벽 위치 정보 담기
for y in range(8):
    for x in range(8):
        if board[y][x] == '#':
            walls_lst.append((x, y))

print(int(game(walls_lst)))
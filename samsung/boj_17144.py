def clean():
    global board
    y1, y2 = cleaner[0], cleaner[1]
    for y in range(y1-2, -1, -1):
        board[y+1][0] = board[y][0]
    for x in range(1, C):
        board[0][x-1] = board[0][x]
    for y in range(1, y1+1):
        board[y-1][C-1] = board[y][C-1]
    for x in range(C-2, 0, -1):
        board[y1][x+1] = board[y1][x]

    for y in range(y2+1, R):
        board[y-1][0] = board[y][0]
    for x in range(1, C):
        board[R-1][x-1] = board[R-1][x]
    for y in range(R-2, y2-1, -1):
        board[y + 1][C - 1] = board[y][C - 1]
    for x in range(C-2, 0, -1):
        board[y2][x + 1] = board[y2][x]


def spread():
    global board, dx, dy
    add_dust = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if board[y][x] >= 5:
                add_dust_num = board[y][x]//5
                for i in range(4):
                    tx, ty = x+dx[i], y+dy[i]
                    if 0 <= tx < C and 0 <= ty < R and board[ty][tx] != -1:
                        add_dust[ty][tx] += add_dust_num
                        add_dust[y][x] -= add_dust_num
    return add_dust


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

for y in range(R):
    if board[y][0] == -1:
        cleaner.append(y)

for _ in range(T):
    dust = []
    temp = spread()
    for y in range(R):
        for x in range(C):
            board[y][x] += temp[y][x]
    clean()
    board[cleaner[0]][1] = 0
    board[cleaner[1]][1] = 0
    board[cleaner[0]][0] = -1
    board[cleaner[1]][0] = -1
ans = 0
for y in range(len(board)):
    ans += sum(board[y])
ans += 2
print(ans)
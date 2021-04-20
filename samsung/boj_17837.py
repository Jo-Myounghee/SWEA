def check(nx, ny):
    if len(horse_board[ny][nx]) >= 4:
        return True
    return False

def isBoard(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or color_board[y][x] == 2:
        return False
    return True

def movecolor(tx, ty, move_items, type):
    global horses, horse_board
    while move_items:
        horse = move_items.pop(type)
        horse_board[ty][tx].append(horse)
        horse_idx = horse[0] - 1
        horses[horse_idx][0] = ty
        horses[horse_idx][1] = tx
def move(_i):
    global horses, horse_board
    ny, nx, nd = horses[_i]
    idx = horse_board[ny][nx].index([_i + 1, nd])
    move_items = horse_board[ny][nx][idx:]
    if check(nx, ny):
        return True
    horse_board[ny][nx] = horse_board[ny][nx][0:idx]

    tx, ty = nx + dx[nd], ny + dy[nd]

    if isBoard(tx, ty):
        if color_board[ty][tx] == 0:
            movecolor(tx, ty, move_items, 0)
        elif color_board[ty][tx] == 1:
            movecolor(tx, ty, move_items, -1)
        if check(tx, ty):
            return True
    else:
        if nd % 2:
            nd = (nd + 3) % 4
        else:
            nd = (nd + 1) % 4
        horses[_i][2] = nd
        for i in range(len(move_items)):
            if move_items[i][0] - 1 == _i:
                move_items[i][1] = nd
        tx, ty = nx + dx[nd], ny + dy[nd]
        if isBoard(tx, ty):
            if color_board[ty][tx] == 0:
                movecolor(tx, ty, move_items, 0)
            elif color_board[ty][tx] == 1:
                movecolor(tx, ty, move_items, -1)
            if check(tx, ty):
                return True
        else:
            while move_items:
                horse = move_items.pop(0)
                if horse[0] - 1 == _i:
                    horse[1] = nd
                horse_board[ny][nx].append(horse)
            if check(nx, ny):
                return True
    return False

N, K = map(int, input().split())
color_board = [list(map(int, input().split())) for _ in range(N)]
horses = [list(map(int, input().split())) for _ in range(K)]
horse_board = [[list() for _ in range(N)] for _ in range(N)]
dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)
for i in range(1, K + 1):
    y, x, dir = horses[i - 1]
    horse_board[y - 1][x - 1].append([i, dir - 1])
    horses[i - 1] = [y - 1, x - 1, dir - 1]
ans = 1
isAns = False
while not isAns:
    if ans > 1000:
        break
    for i in range(K):
        isAns = move(i)
        if isAns:
            break
    if not isAns:
        ans += 1
if isAns:
    print(ans)
else:
    print(-1)

'''
7 10
0 1 1 0 1 1 2
1 1 0 1 1 0 1
2 1 0 1 1 0 1
1 0 1 1 0 2 0
2 0 1 2 0 1 0
0 2 1 0 2 1 0
0 0 0 1 0 1 0
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1
-> 9
'''
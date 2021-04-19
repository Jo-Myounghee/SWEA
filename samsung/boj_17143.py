def isBoard(x, y):
    if 0 <= x < C and 0 <= y < R:
        return True
    return False

def move(x, y, s, d, z):
    global board, sharks

    for i in range(s):
        if isBoard(x+dir[d][0], y+dir[d][1]):
            x += dir[d][0]
            y += dir[d][1]
        else:
            if d%2:
                d = (d+1)%4
            else:
                d = (d+3)%4
            x += dir[d][0]
            y += dir[d][1]

    if board[y][x] > z:
        return False
    return (x, y, d)



R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
sharks.sort(key=lambda x : x[4], reverse=True)
# r(y), c(x), s(속력), d(방향), z(크기)


dir = ((-1, 0), (0, -1), (0, 1), (1, 0))

board = [[0]*C for _ in range(R)]
for i in range(M):
    y, x, s, d, z = sharks[i]
    board[y-1][x-1] = z

ans = 0
for t in range(C):
    # 상어 잡음
    for y in range(R):
        if board[y][t] != 0:
            ans += board[y][t]
            board[y][t] = 0
            for i in range(len(sharks)):
                _y, _x = sharks[i][0]-1, sharks[i][1]-1
                if y == _y and t == _x:
                    sharks[i] = [0]*5
            break

    # 상어 이동 -> 만약 이미 상어가 존재한다면 -> 작은 상어 죽이기
    board = [[0]*C for _ in range(R)]
    for i in range(M):
        if sharks[i] != [0]*5:
            y, x, s, d, z = sharks[i]
            y -= 1
            x -= 1
            d %= 4
            can_move = move(x, y, s, d, z)
            if not can_move:
                sharks[i] = [0] * 5
            else:
                tx, ty, d = can_move
                board[ty][tx] = z
                sharks[i] = [ty+1, tx+1, s, d, z]
print(ans)
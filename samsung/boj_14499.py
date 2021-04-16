def isWall(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return True
    return False

def move():
    global dirs
    dir = dirs[0]
    if dir == 1:
        return (1, 0)
    elif dir == 2:
        return (-1, 0)
    elif dir == 3:
        return (0, -1)
    elif dir == 4:
        return (0, 1)

def rotate():
    global dirs, nx, ny
    while dirs:
        dx, dy = move()
        tx = nx + dx
        ty = ny + dy

        if not isWall(tx, ty):
            if (dx, dy) == (1, 0):
                dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
            elif (dx, dy) == (-1, 0):
                dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
            elif (dx, dy) == (0, 1):
                dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
            elif (dx, dy) == (0, -1):
                dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]

            # 만약 board가 0이라면 -> 주사위 바닥에 있는 글씨를 보드로 복사 (주사위 바닥은 그대로 있는거)
            if board[ty][tx] == 0:
                board[ty][tx] = dice[1]
            # 만약 board에 숫자가 있다면 -> board에 쓰여있는 숫자가 주사위 바닥으로 복사되고,칸에 쓰인 숫자는 0이 됨.
            else:
                dice[1] = board[ty][tx]
                board[ty][tx] = 0
            nx, ny = tx, ty
            ans.append(dice[6])
        dirs.pop(0)

N, M, sx, sy, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = list(map(int, input().split()))
dice = [0] * 7
nx, ny = sx, sy
ans = []

rotate()
print(*ans, sep="\n")
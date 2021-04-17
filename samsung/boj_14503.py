def isBoard(x, y):
    if 0 <= x < M and 0 <= y < N:
        return True
    return False

def canClean(x, y):
    if isBoard(x, y):
        if visited[y][x] == 0 and board[y][x] != 1:
            return True
    return False

def rotateRobot(dir):
    return (dir+3)%4

def clean(x, y, d, cnt):
    global visited
    if visited[y][x] == 0:
        visited[y][x] = cnt

    for _ in range(4):
        nd = rotateRobot(d)
        nx = x + direction[nd][0]
        ny = y + direction[nd][1]
        if canClean(nx, ny):
            clean(nx, ny, nd, cnt+1)
            return
        else:
            d = nd
            continue

    nx = x - (direction[nd][0])
    ny = y - (direction[nd][1])
    no_cnt = 0
    for i in range(4):
        tx = nx + direction[nd][0]
        ty = ny + direction[nd][1]
        if visited[ty][tx] != 0 or board[ty][tx] == 1:
            no_cnt += 1

    if no_cnt == 4:
        if board[ny][nx] == 1:
            print(cnt)
            exit()
    if visited[ny][nx] == 0:
        clean(nx, ny, nd, cnt+1)
    else:
        clean(nx, ny, nd, cnt)



N, M = map(int, input().split())
sy, sx, sd = map(int, input().split())
# 북 동 남 서
direction = ((0, -1), (1, 0), (0, 1), (-1, 0))
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0
clean(sx, sy, sd, 1)

'''
6 6
2 1 3
1 1 1 1 1 1
1 0 0 0 0 1
1 0 1 1 1 1
1 0 1 1 1 1
1 0 1 1 1 1
1 1 1 1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

6 6
2 1 3
1 1 1 1 1 1
1 0 0 0 0 1
1 0 1 1 1 1
1 0 1 1 1 1
1 0 1 1 1 1
1 1 1 1 1 1

6 7
2 1 0
1 1 1 1 1 1 1
1 0 0 0 0 0 1
1 0 1 0 1 0 1
1 1 0 1 1 0 1
1 0 0 0 0 0 1
1 1 1 1 1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
def check(x, y):
    global board
    # 가로
    cnt = [0] * 10
    for _x in range(9):
        now_val = board[y][_x]
        if now_val != 0:
            cnt[now_val] += 1
            if cnt[now_val] > 1:
                return False
    # 세로
    cnt = [0] * 10
    for _y in range(9):
        now_val = board[_y][x]
        if now_val != 0:
            cnt[now_val] += 1
            if cnt[now_val] > 1:
                return False
    # 3x3
    cnt = [0] * 10
    for _y in range((y//3)*3, (y//3)*3+3):
        for _x in range((x//3)*3, (x//3)*3+3):
            now_val = board[_y][_x]
            if now_val != 0:
                cnt[now_val] += 1
                if cnt[now_val] > 1:
                    return False
    return True

def dfs(cnt):
    global board
    if cnt == N:
        for i in range(9):
            print(*board[i])
        exit()

    nx, ny = bin_lst[cnt]
    for i in range(1, 10):
        board[ny][nx] = i
        if check(nx, ny):
            dfs(cnt+1)
        board[ny][nx] = 0


board = [list(map(int, input().split())) for _ in range(9)]
bin_lst = []
for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            bin_lst.append((x, y))
N = len(bin_lst)
dfs(0)
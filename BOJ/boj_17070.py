def ispipe(x, y, pipe):
    global ans, N
    if x == N-1 and y == N-1:
        ans += 1

    if pipe == 0:
        if x+1 < N and board[y][x+1] != 1:
            ispipe(x+1, y, 0)
            if y+1 < N and board[y+1][x] != 1 and board[y+1][x+1] != 1:
                ispipe(x+1, y+1, 2)
    elif pipe == 1:
        if y+1 < N and board[y+1][x] != 1:
            ispipe(x, y+1, 1)
            if x+1 < N and board[y][x+1] != 1 and board[y+1][x+1] != 1:
                ispipe(x+1, y+1, 2)
    elif pipe == 2:
        if x+1 < N and board[y][x+1] != 1:
            ispipe(x+1, y, 0)
        if y+1 < N and board[y+1][x] != 1:
            ispipe(x, y+1, 1)
            if x+1 < N and board[y][x+1] != 1 and board[y+1][x+1] != 1:
                ispipe(x+1, y+1, 2)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

ispipe(1, 0, 0)
print(ans)
'''0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'''
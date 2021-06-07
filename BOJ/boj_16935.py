'''
6 8 6
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
1 2 3 4 5 6
'''

def func(c):
    def clock_rotate(b):
        _N, _M = len(b), len(b[0])
        temp_board = [[0] * _N for _ in range(_M)]
        for y in range(_M):
            for x in range(_N):
                temp_board[y][x] = b[_N-1-x][y]
        return temp_board

    def block_rotate(b, n):
        _M, _N = len(b[0]), len(b)
        temp_board = [[0] * _M for _ in range(_N)]
        group_1 = [b[i][:_M // 2] for i in range(_N // 2)]
        group_2 = [b[i][_M // 2:] for i in range(_N // 2)]
        group_3 = [b[i][_M // 2:] for i in range(_N // 2, _N)]
        group_4 = [b[i][:_M // 2] for i in range(_N // 2, _N)]

        if n == 5:
            lst = [group_1, group_2, group_3, group_4]
        else:
            lst = [group_3, group_4, group_1, group_2]

        # 2 <- 1
        for i in range(_N//2):
            temp_board[i][_M//2:] = lst[0][i]
        # 3 <- 2
        for i in range(_N//2, _N):
            temp_board[i][_M//2:] = lst[1][i-(_N//2)]
        # 4 <- 3
        for i in range(_N//2, _N):
            temp_board[i][:_M//2] = lst[2][i-(_N//2)]
        # 1 <- 4
        for i in range(_N//2):
            temp_board[i][:_M//2] = lst[3][i]

        return temp_board

    if c in [3, 4, 5, 6]:
        temp = [board[i][:] for i in range(len(board))]
        if c == 3:
            temp = clock_rotate(temp)
        elif c == 4:
            for _ in range(3):
                temp = clock_rotate(temp)
        elif c == 5:
            temp = block_rotate(temp, c)
        elif c == 6:
            temp = block_rotate(temp, c)
    else:
        temp = [[0] * len(board[0]) for _ in range(len(board))]
        if c == 1:
            for y in range(len(board)):
                temp[y] = board[len(board) - 1 - y]

        elif c == 2:
            for y in range(len(board)):
                for x in range(len(board[0])):
                    temp[y][x] = board[y][len(board[0]) - 1 - x]

    return temp


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))

for c in C:
    board = func(c)
for i in range(len(board)):
    print(*board[i])

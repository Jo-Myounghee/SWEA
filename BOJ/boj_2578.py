board = [list(map(int, input().split())) for _ in range(5)]
# board_row = [x for x in zip(*board_col)]
board_cro = [[board[x][x] for x in range(5)], [board[x][4-x] for x in range(5)]]

NUMS = [list(map(int, input().split())) for _ in range(2)]

def check(num):
    for i in range(5):
        if board[i].count(num):
            board[i][board[i].index(num)] = 0
            break
    cnt = 0
    for i in range(5):
        if board[i].count(0) == 5:
            cnt += 1
        board_row = [x for x in zip(*board)]
        if board_row[i].count(0) == 5:
            cnt += 1
        board_cro = [[board_col[x][x] for x in range(5)], [board_col[x][4 - x] for x in range(5)]]
        for j in range(2):
            if board_cro[j].count(0) == 5:
                cnt += 1
    if cnt == 5
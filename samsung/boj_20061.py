def solve(block_type, c, board):
    global scores
    r = 0
    # 블록 내리기
    while True:
        if block_type == 2:
            if r == 5 or board[r + 1][c] or board[r + 1][c + 1]:
                break
            else:
                r += 1
        else:
            if r == 5 or board[r + 1][c]:
                break
            else:
                r += 1

    board[r][c] = 1
    if block_type == 2:
        board[r][c + 1] = 1
    elif block_type == 3:
        board[r - 1][c] = 1

    # 줄 없애기
    full_row = []
    for i in range(6):
        if sum(board[i]) == 6:
            full_row.append(i)
            scores += 1

    while full_row:
        idx = full_row.pop()
        board.pop(idx)
        board.insert(0, [0]*4)

    # 0, 1행 확인
    while True:
        if sum(board[1]) != 0:
            board.pop()
            board.insert(0, [0]*4)
        else:
            break

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
scores = 0
green_board = [[0 for _ in range(4)] for _ in range(6)]
blue_board = [[0 for _ in range(4)] for _ in range(6)]

for block_type, x, y in blocks:
    solve(block_type, y, green_board)

    if block_type == 1:
        solve(block_type, 3 - x, blue_board)
    elif block_type == 2:
        solve(3, 3 - x, blue_board)
    elif block_type == 3:
        solve(2, 3 - x - 1, blue_board)

total_block = 0
for i in range(6):
    total_block += sum(green_board[i])
    total_block += sum(blue_board[i])

print(scores, total_block, sep="\n")
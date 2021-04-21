def isGreen(x, y):
    if 0 <= y < 4 and 0 <= x < 6:
        return True
    return False

def isBlue(x, y):
    if 0 <= y < 6 and 0 <= x < 4:
        return True
    return False

def green(t, x, y):
    global score
    tx = 0
    if t == 1:
        while isGreen(tx, y) and green_board[tx][y] == 0:
            tx += 1

    elif t == 2:
        while isGreen(tx, y+1) and green_board[tx][y] == 0 and green_board[tx][y+1] == 0:
            tx += 1
        green_board[tx - 1][y+1] = 1

    elif t == 3:
        while isGreen(tx+1, y) and green_board[tx+1][y] == 0:
            tx += 1
        green_board[tx][y] = 1
    green_board[tx - 1][y] = 1

    print('초록색 보드에 블록 쌓기')
    for i in range(len(green_board)):
        print(green_board[i])
    print('------------------------')

    full_row = []
    for i in range(6):
        if sum(green_board[i]) == 4:
            full_row.append(i)
            score += 1

    while full_row:
        i = full_row.pop(0)
        green_board.pop(i)
        green_board.insert(0, [0, 0, 0, 0])

    print('초록색 보드 한 줄 찬거 정리')
    for i in range(len(green_board)):
        print(green_board[i])
    print('------------------------')

    exist_row = [False]*2
    for i in range(1, -1, -1):
        if sum(green_board[i]) > 0:
            exist_row[i] = True
    for i in range(2):
        if exist_row[i]:
            green_board.pop()
            green_board.insert(0, [0, 0, 0, 0])

    print('초록색 0, 1번째 줄에 있을 경우 마지막 꺼 빼주기')
    for i in range(len(green_board)):
        print(green_board[i])
    print('------------------------')

def blue(t, x, y):
    global score
    ty = 0
    if t == 1:
        while isBlue(x, ty) and blue_board[x][ty] == 0:
            ty += 1

    elif t == 2:
        while isBlue(x, ty+1) and blue_board[x][ty+1] == 0:
            ty += 1
        blue_board[x][ty] = 1

    elif t == 3:
        while isBlue(x+1, ty) and blue_board[x][ty] == 0 and blue_board[x+1][ty] == 0:
            ty += 1
        blue_board[x+1][ty-1] = 1
    blue_board[x][ty - 1] = 1

    print('파란색 보드 블록 쌓기')
    for i in range(len(blue_board)):
        print(blue_board[i])
    print('------------------------')

    full_col = []
    for i in range(6):
        temp_cnt = 0
        for j in range(4):
            if blue_board[j][i] == 1:
                temp_cnt += 1
        if temp_cnt == 4:
            full_col.append(i)

    while full_col:
        i = full_col.pop()
        for j in range(4):
            blue_board[j].pop(i)
            blue_board[j].insert(0, 0)
        score += 1

    print('파란색 보드 한 열 쌓인거 빼기')
    for i in range(len(blue_board)):
        print(blue_board[i])
    print('------------------------')

    exist_col = [False]*2
    for i in range(2):
        for j in range(4):
            if blue_board[j][i] == 1:
                exist_col[i] = True

    for i in range(1, -1, -1):
        if exist_col[i]:
            for j in range(4):
                blue_board[j].pop()
                blue_board[j].insert(0, 0)

    print('파란색 보드 0, 1열에 있는 경우 빼주고 앞에다가 집어 넣기')
    for i in range(len(blue_board)):
        print(blue_board[i])
    print('------------------------')

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
red_board = [[0]*4 for _ in range(4)]
blue_board = [[0]*6 for _ in range(4)]
green_board = [[0]*4 for _ in range(6)]

score = 0
total_block = 0

while blocks:
    t, x, y = blocks.pop(0)
    print('type', t, 'x', x, 'y', y)
    blue(t, x, y)
    green(t, x, y)

for i in range(6):
    if i < 4:
        total_block += sum(blue_board[i])
    total_block += sum(green_board[i])

print(score, total_block, sep="\n")

'''
12
2 0 0
2 0 1
2 0 2
2 0 0
2 0 1
2 0 2
2 0 0
2 0 1
2 0 2
2 0 0
2 0 1
2 0 2
'''
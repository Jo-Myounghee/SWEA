def funcC():
    global board
    board = rotate(board)
    funcR()
    board = rotate(board)

def rotate(inlst):
    outlst = [[0]*len(inlst) for _ in range(len(inlst[0]))]
    for y in range(len(inlst)):
        for x in range(len(inlst[0])):
            outlst[x][y] = inlst[y][x]
    return outlst

def funcR():
    global board
    temp_board = []
    max_length = 0

    for i in range(len(board)):
        temp_set = list(set(board[i]))
        temp = []
        for idx in range(len(temp_set)):
            if temp_set[idx] == 0:
                continue
            temp_cnt = board[i].count(temp_set[idx])
            temp.append([temp_set[idx], temp_cnt])

        temp.sort(key=lambda x : (x[1], x[0]))
        t = len(temp)
        for i in range(t):
            x, y = temp.pop(0)
            temp.append(x)
            temp.append(y)
        temp_board.append(temp)
        max_length = max(max_length, len(temp))

    for i in range(len(temp_board)):
        length = len(temp_board[i])
        if len(temp_board[i]) < max_length:
            temp_board[i] += [0]*(max_length-length)
    board = temp_board

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
total_time = 0
while True:
    try:
        if board[r-1][c-1] == k:
            print(total_time)
            break
        else:
            total_time += 1
    except:
        total_time += 1

    if total_time > 100:
        print(-1)
        break

    if len(board) >= len(board[0]):
        funcR()

    else:
        funcC()


'''
4 4 1
1 2 1
2 1 3
3 3 3
'''
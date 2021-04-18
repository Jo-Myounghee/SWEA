def isBoard(x, y):
    if x < 0 or x >= M or y < 0 or y >= N or board[y][x] == 6:
        return False
    return True

def countBoard(b):
    global minAns
    cnt = 0
    for y in range(N):
        for x in range(M):
            if b[y][x] == 0:
                cnt += 1
    minAns = min(minAns, cnt)
    return

def installCctv(cnt, origin_board):
    # global board
    if cnt == len(cctv):
        print('여기')
        # 현재 board에서 사각 지대 부분 숫자 세기 고고
        for i in range(N):
            print(origin_board[i])
        countBoard(origin_board)
        return
    cx, cy, type = cctv[cnt]
    board = [origin_board[i][:] for i in range(N)]
    if type == 1:
        for i in range(4):
            if i == 0:
                for _x in range(cx+1, M):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                installCctv(cnt+1, board)
                board = [origin_board[i][:] for i in range(N)]
            elif i == 1:
                for _x in range(cx-1, -1, -1):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                installCctv(cnt + 1, board)
                board = [origin_board[i][:] for i in range(N)]
            elif i == 2:
                for _y in range(cy+1, N):
                    if isBoard(cx, _y):
                        board[_y][cx] = True
                    else:
                        break
                installCctv(cnt + 1, board)
                board = [origin_board[i][:] for i in range(N)]
            elif i == 3:
                for _y in range(cy-1, -1, -1):
                    if isBoard(cx, _y):
                        board[_y][cx] = True
                    else:
                        break
                installCctv(cnt + 1, board)
                board = [origin_board[i][:] for i in range(N)]
    elif type == 2:
        for i in range(2):
            if i == 0:
                # 가로
                for _x in range(cx+1, M):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                for _x in range(cx-1, -1, -1):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                installCctv(cnt + 1, board)
                board = [origin_board[i][:] for i in range(N)]
            else:
                # 세로
                for _y in range(cy+1, N):
                    if isBoard(cx, _y):
                        board[_y][cx] = True
                    else:
                        break
                for _y in range(cy-1, -1, -1):
                    if isBoard(cx, _y):
                        board[_y][cx] = True
                    else:
                        break
                installCctv(cnt + 1, board)
                board = [origin_board[i][:] for i in range(N)]
    elif type == 3:
        # 1
        for i in range(4):
            if i < 2 :
                for _x in range(cx + 1, M):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                if i == 0:
                    for _y in range(cy - 1, -1, -1):
                        if isBoard(cx, _y):
                            board[_y][cx] = True
                        else:
                            break
                elif i == 1:
                    for _y in range(cy + 1, N):
                        if isBoard(cx, _y):
                            board[_y][cx] = True
                        else:
                            break
            else:
                for _x in range(cx - 1, -1, -1):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                if i == 2:
                    for _y in range(cy - 1, -1, -1):
                        if isBoard(cx, _y):
                            board[_y][cx] = True
                        else:
                            break
                elif i == 3:
                    for _y in range(cy + 1, N):
                        if isBoard(cx, _y):
                            board[_y][cx] = True
                        else:
                            break
            installCctv(cnt + 1, board)
            board = [origin_board[i][:] for i in range(N)]
    elif type == 4:
        for i in range(4):
            if i < 3:
                for _x in range(cx+1, M):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                for _x in range(cx-1, -1, -1):
                    if isBoard(_x, cy):
                        board[cy][_x] = True
                    else:
                        break
                if i == 0:
                    for _y in range(cy-1, -1, -1):
                        if isBoard(cx, _y):
                            board[_y][cx] = True
                        else:
                            break
                    installCctv(cnt + 1, board)
                    board = [origin_board[i][:] for i in range(N)]
                else:
                    for _y in range(cy+1, N):
                        if isBoard(cx, _y):
                            board[_y][cx] = True
                        else:
                            break
                    installCctv(cnt + 1, board)
                    board = [origin_board[i][:] for i in range(N)]
            else:
                for _y in range(cy - 1, -1, -1):
                    if isBoard(cx, _y):
                        board[_y][cx] = True
                    else:
                        break
                for _y in range(cy + 1, N):
                    if isBoard(cx, _y):
                        board[_y][cx] = True
                    else:
                        break
                if i == 2:
                    for _x in range(cx + 1, M):
                        if isBoard(_x, cy):
                            board[cy][_x] = True
                        else:
                            break
                    installCctv(cnt + 1, board)
                    board = [origin_board[i][:] for i in range(N)]
                else:
                    for _x in range(cx - 1, -1, -1):
                        if isBoard(_x, cy):
                            board[cy][_x] = True
                        else:
                            break
                    installCctv(cnt + 1, board)
                    board = [origin_board[i][:] for i in range(N)]
    elif type == 5:
        for _x in range(cx + 1, M):
            if isBoard(_x, cy):
                board[cy][_x] = True
            else:
                break
        for _x in range(cx - 1, -1, -1):
            if isBoard(_x, cy):
                board[cy][_x] = True
            else:
                break
        for _y in range(cy - 1, -1, -1):
            if isBoard(cx, _y):
                board[_y][cx] = True
            else:
                break
        for _y in range(cy + 1, N):
            if isBoard(cx, _y):
                board[_y][cx] = True
            else:
                break
        installCctv(cnt + 1, board)
        board = [origin_board[i][:] for i in range(N)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv = []
minAns = 1e9
for y in range(N):
    for x in range(M):
        if board[y][x] != 0 and board[y][x] != 6:
            cctv.append([x, y, board[y][x]])

print(cctv)
installCctv(0, board)
print(minAns)
# for i in range(len(cctv)):
#     cx, cy, ct = cctv[i]

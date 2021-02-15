def changePaper(n, x, y):
    for i in range(1, n):


def isCorrect(x, y):
    # 2x2
    if board[y][x] == 2:
        dir = [[0, 1], [1, 1], [1, 0]]
        for i in range(len(dir)):
            test_x = x + dir[i][0]
            test_y = y + dir[i][1]
            if 0 <= test_x < 10 and 0 <= test_y < 10 and [test_y][test_x] != 2 :
                return False


    elif board[y][x] == 3:
        dir = [[0, 1], [1, 1], [1, 0], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0]]
        for i in range(len(dir)):
            test_x = x + dir[i][0]
            test_y = y + dir[i][1]
            if 0 <= test_x < 10 and 0 <= test_y < 10 and board[test_y][test_x] != 3 :
                return False

    elif board[y][x] == 4:
        dir = [[0, 1], [1, 1], [1, 0], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [0, 3], [1, 3], [2, 3], [3, 3], [3, 2], [3, 1], [3, 0]]
        for i in range(len(dir)):
            test_x = x + dir[i][0]
            test_y = y + dir[i][1]
            if 0 <= test_x < 10 and 0 <= test_y < 10 and board[test_y][test_x] != 4 :
                return False

    elif board[y][x] == 5:
        dir = [[0, 1], [1, 1], [1, 0], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [0, 3], [1, 3], [2, 3], [3, 3], [3, 2], [3, 1], [3, 0], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0]]
        for i in range(len(dir)):
            test_x = x + dir[i][0]
            test_y = y + dir[i][1]
            if 0 <= test_x < 10 and 0 <= test_y < 10 and board[test_y][test_x] != 5 :
                return False

    return True

def paperPatch(x, y):
    global board, papers

    # 1x1
    # board[test_y][test_x] = 1

    # 5x5
    if 0<=x+4 <10 and 0<=y+4< 10:
        dir = [[0, 1], [1, 1], [1, 0], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [0, 3], [1, 3], [2, 3], [3, 3], [3, 2], [3, 1], [3, 0], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0]]
        for i in range(len(dir)):
            test_x = x + dir[i][0]
            test_y = y + dir[i][1]
            board[test_y][test_x] = 5

    # 2x2
    if 0<=x+1<10 and 0<=y+1<10 and board[y+1][x+1] > 0:
        dir = [[0, 1], [1, 1], [1, 0]]
        for i in range(len(dir)):
            test_x = x + dir[i][0]
            test_y = y + dir[i][1]
            if board[test_y][test_x] > 0 :
                board[test_y][test_x] = 2

    # 3x3
        if 0<=x+2<10 and 0<=y+2<10 and board[test_y][test_x] == 1:
            dir = [[0, 2], [1, 2], [2, 2], [2, 1], [2, 0]]
            for i in range(len(dir)):
                test_x = x + dir[i][0]
                test_y = y + dir[i][1]
                if board[test_y][test_x] > 0:
                    board[test_y][test_x] = 3
    # 4x4
            if 0 <= x+3 < 10 and 0 <= y+3< 10 and board[test_y][test_x] == 1:
                dir = [[0, 3], [1, 3], [2, 3], [3, 3], [3, 2], [3, 1], [3, 0]]
                for i in range(len(dir)):
                    test_x = x + dir[i][0]
                    test_y = y + dir[i][1]
                    if board[test_y][test_x] > 0:
                        board[test_y][test_x] = 4


    # # 하우
    # for j in range(5):
    #     test_x = x + j
    #     test_y = y + j
    #     if 0 <= test_x < 10 and 0 <= test_y < 10 and board[test_y][test_x] == 1:
    #         dir = [[1, 0], [0, 1]]
    #         for k in range(0, j):
    #             for i in range(2):
    #                 test_x = x + dir[i][0] * k
    #                 test_y = y + dir[i][1] * k


    # 다섯개짜리

    # 네개짜리
    # 세개짜리
    # 두개짜리
    # 한개짜리
board = [list(map(int, input().split())) for _ in range(10)]

papers = [0] + [5] * 5

for y in range(10):
    for x in range(10):
        if board[y][x] == 1:

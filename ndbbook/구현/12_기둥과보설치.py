# input
'''
n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
'''
# 기둥 설치 가능한가
def column_make_possible(test_x, test_y):
    global board
    if test_y == 0:
        return True
    elif board[test_y-1][test_x] == 0:
        return True
    elif board[test_y][test_x-1] == 1:
        return True
    return False

# 보 설치 가능한가
def bar_make_possible(test_x, test_y):
    global board
    if board[test_y][test_x-1] == 1 and board[test_y][test_x+1] == 1:
        return True
    elif board[test_y-1][test_x] == 0:
        return True
    elif board[test_y-1][test_x+1] == 0:
        return True
    return False

# 기둥 삭제 가능한가
def column_del_possible(test_x, test_y):
    global board
    if board[test_y+1][test_x-1] == 1:
        return False
    elif board[test_y+1][test_x] == 1 or board[test_y+1][test_x] == 0:
        return False
    return True

# 보 삭제 가능한가
def bar_del_possible(test_x, test_y):
    global board
    if board[test_y][test_x-1] == 1:
        return False
    elif board[test_y][test_x+1] == 1:
        return False
    elif board[test_y][test_x+1] == 0 and board[test_y-1][test_x+1] != 0:
        return False
    return True

def solution(n, build_frame):
    global board
    answer = []
    board = [[-2]*(n+1) for _ in range(n+1)]
    for i in range(len(build_frame)):
        test_x = build_frame[i][0]
        test_y = build_frame[i][1]
        print(test_x, test_y)
        # 설치할 때
        if build_frame[i][3] == 1:
            # 기둥 설치할 때
            if build_frame[i][2] == 0:
                if column_make_possible(test_x, test_y):
                    board[test_y][test_x] = 0
            # 보 설치할 때
            else:
                if bar_make_possible(test_x, test_y):
                    board[test_y][test_x] = 1
        # 구조물 삭제할 때
        else:
            # 삭제할 구조물이 기둥일 때
            if build_frame[i][2] == 0:
                if column_del_possible(test_x, test_y):
                    # 삭제 가능한지 알아보는 조건문 넣어주기
                    board[test_y][test_x] = -2
            # 삭제할 구조물이 보일 때
            else:
                if bar_del_possible(test_x, test_y):
                    # 삭제 간으한지 알아보는 조건문 넣어주기
                    board[test_y][test_x] = -2
    # for i in range(n+1):
    #     print(*board[i])
    for x in range(n+1):
        for y in range(n+1):
            if board[y][x] == 0:
                answer.append([x, y, 0])
            elif board[y][x] == 1:
                answer.append([x, y, 1])
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))

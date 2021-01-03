import sys
sys.stdin = open('118input.txt', 'r')

def isPath(x, y):
    if 0 <= x < N and 0 <= y < M and board[y][x] != 1:
        return True
    return False

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

N, M = map(int, input().split())
now_x, now_y, dir = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dir_lst = [[0, -1], [1, 0], [0, 1], [-1, 0]] # 북 동 남 서

board[now_y][now_x] = 1

cnt = 1
turn_time = 0
while True:
    turn_left()
    test_x = now_x + dir_lst[dir][0]
    test_y = now_y + dir_lst[dir][1]
    if isPath(test_x, test_y):
        board[test_y][test_x] = 1
        now_x = test_x
        now_y = test_y
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        test_x = now_x - dir_lst[dir][0]
        test_y = now_y - dir_lst[dir][1]
        if isPath(test_x, test_y):
            now_x = test_x
            now_y = test_y
        else:
            break
        turn_time = 0
print(cnt)
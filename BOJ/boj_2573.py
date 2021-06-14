from collections import deque


def is_road(x, y):
    global N, M
    if 0 <= x < M and 0 <= y < N:
        return True
    return False


def melt_ice(q):
    global board
    q_len = len(q)
    for i in range(q_len):
        x, y, val = q.popleft()
        melting_cnt = 0
        for _d in range(4):
            tx, ty = x + dir_lst[_d][0], y + dir_lst[_d][1]
            if is_road(tx, ty) and board[ty][tx] == 0:
                melting_cnt += 1
        val = max(0, val-melting_cnt)
        if val > 0:
            q.append((x, y, val))

    board = [[0]*M for _ in range(N)]
    for x, y, val in q:
        board[y][x] = val
    return q


def is_twice(sx, sy):
    global board, N, M, dir_lst
    copy_board = [board[i][:] for i in range(N)]

    copy_q = deque()
    copy_q.append((sx, sy))
    copy_board[sy][sx] = 0

    while copy_q:
        nx, ny = copy_q.popleft()
        for i in range(4):
            tx, ty = nx + dir_lst[i][0], ny + dir_lst[i][1]
            if is_road(tx, ty) and copy_board[ty][tx] > 0:
                copy_q.append((tx, ty))
                copy_board[ty][tx] = 0

    temp_sum = 0
    for y in range(N):
        temp_sum += sum(copy_board[y])

    if temp_sum > 0:
        return True
    return False


def func(ice_lst):
    q = deque(ice_lst)
    answer = 1

    while q:
        q = melt_ice(q)
        if q:
            sx, sy = q[0][0], q[0][1]
            if is_twice(sx, sy):
                return answer
            else:
                answer += 1
    return 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ice = []
dir_lst = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for y in range(N):
    for x in range(M):
        if board[y][x] > 0:
            ice.append((x, y, board[y][x]))
print(func(ice))

'''
5 5
0 0 0 0 0
0 0 10 10 0
0 10 0 10 0
0 0 10 10 0
0 0 0 0 0
-> 1

3 4 
0 0 0 0
0 3 5 0
0 0 0 0

'''
'''
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
'''
def isBoard(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def game(sx, sy, sd):
    score = 0
    tx, ty, nd = sx, sy, sd

    while True:
        tx, ty = tx + dir[nd][0], ty + dir[nd][1]
        if isBoard(tx, ty):
            # 만약 블록을 만났을 경우
            if board[ty][tx] in range(1, 6):
                block_type = board[ty][tx]
                # 점수 증가
                score += 1
                nd = block_dir[block_type][nd]
                continue
            # 만약 웜홀을 만났을 경우
            elif board[ty][tx] in range(6, 11):
                hall_type = board[ty][tx]
                if (tx, ty) == hall[hall_type][0]:
                    tx, ty = hall[hall_type][1]
                else:
                    tx, ty = hall[hall_type][0]
                continue
            # 만약 블랙홀을 만났을 경우
            elif board[ty][tx] == -1:
                return score
            # 시작점일 경우
            elif (tx, ty) == (sx, sy):
                return score
            # 만약 그냥 빈 칸인 경우
            else:
                continue
        # 벽을 만났을 경우
        else:
            nd = (nd+2)%4
            score += 1

dir = ((0, -1), (1, 0), (0, 1), (-1, 0))    # 위 오른쪽 아래 왼쪽
block_dir = [[],
             [2, 3, 1, 0],
             [1, 3, 0, 2],
             [3, 2, 0, 1],
             [2, 0, 3, 1],
             [2, 3, 0, 1]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxAns = 0
    # 웜홀 리스트
    hall = [[] for _ in range(11)]
    for y in range(N):
        for x in range(N):
            val = board[y][x]
            if val in range(6, 11):
                hall[val].append((x, y))
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0:
                for i in range(4):
                    score = game(x, y, i)
                    maxAns = max(score, maxAns)
    print('#{} {}'.format(tc, maxAns))

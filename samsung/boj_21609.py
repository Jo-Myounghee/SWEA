from collections import deque


def is_board(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def game():
    global board
    score = 0
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    def find_block_group():
        # 기준 블록 x, 기준 블록 y
        standard_block = (N, N)
        block_group = []
        rainbows = 0
        visited = [[False] * N for _ in range(N)]

        def get_block_group(now_color, sx, sy):
            group = []
            rainbow_cnt = 0
            _standard_block = (sx, sy)
            q = deque()
            q.append((sx, sy))
            visited[sy][sx] = True
            rainbow_visited = [[False] * N for _ in range(N)]

            while q:
                nx, ny = q.popleft()
                group.append((nx, ny))
                for i in range(4):
                    tx, ty = nx + dx[i], ny + dy[i]
                    # if is_board(tx, ty):
                    #     # 무지개라면
                    #     if board[ty][tx] == 0 and not rainbow_visited[ty][tx]:
                    #         rainbow_cnt += 1
                    #         rainbow_visited[ty][tx] += 1
                    #     elif board[ty][tx] == now_color and not visited[ty][tx]:
                    #         if ty < _standard_block[1]:
                    #             _standard_block = (tx, ty)
                    #         elif ty == _standard_block[1] and tx < _standard_block[0]:
                    #             _standard_block = (tx, ty)
                    #         visited[ty][tx] = True
                    #     q.append((tx, ty))

                    if is_board(tx, ty) and not visited[ty][tx] and board[ty][tx] in [0, now_color]:
                        if board[ty][tx] == now_color:
                            if ty < _standard_block[1]:
                                _standard_block = (tx, ty)
                            elif ty == _standard_block[1] and tx < _standard_block[0]:
                                _standard_block = (tx, ty)
                        else:
                            rainbow_cnt += 1
                        q.append((tx, ty))
                        visited[ty][tx] = True
            return group, _standard_block, rainbow_cnt

        for y in range(N):
            for x in range(N):
                if board[y][x] is not None and not visited[y][x] and board[y][x] > 0:
                    temp_block_group, temp_standard_block, temp_rainbows = get_block_group(board[y][x], x, y)
                    # 리스트 정보 갱신 (기준 블록)
                    if len(temp_block_group) > len(block_group):
                        block_group = temp_block_group
                        standard_block = temp_standard_block
                    elif len(temp_block_group) == len(block_group):
                        if rainbows < temp_rainbows:
                            block_group = temp_block_group
                            standard_block = temp_standard_block
                        elif rainbows == temp_rainbows:
                            if standard_block[1] < temp_standard_block[1]:
                                block_group = temp_block_group
                                standard_block = temp_standard_block
                            elif standard_block[1] == temp_standard_block[1] and standard_block[0] < temp_standard_block[0]:
                                block_group = temp_block_group
                                standard_block = temp_standard_block
        return block_group

    def delete_block_group(blocks):
        _score = len(blocks) * len(blocks)
        for block in blocks:
            _x, _y = block[0], block[1]
            board[_y][_x] = None
        return

    def active_gravity():
        for x in range(N):
            col = [board[i][x] for i in range(N)]
            upper = []
            for y in range(N):
                if col[y] is not None:
                    if col[y] != -1:
                        upper.append(col[y])
                        col[y] = None
                    elif col[y] == -1:
                        _idx = 1
                        while upper:
                            col[y - _idx] = upper.pop()
                            _idx += 1
            upper_i = 0
            while upper:
                col[N-1-upper_i] = upper.pop()
                upper_i += 1
            for i in range(N):
                board[i][x] = col[i]
        return
    
    # 반시계 회전
    def rotate_board():
        new = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                new[N - 1 - x][y] = board[y][x]
        return new

    # 이제 여기에 로직 정리
    while True:
        block_group = find_block_group()
        if len(block_group) <= 1:
            break
        delete_block_group(block_group)
        print(block_group, '삭제할 것')
        for i in range(N):
            print(*board[i], '삭제 후')
        # 점수 추가
        score += (len(block_group)**2)
        active_gravity()
        for i in range(N):
            print(*board[i], '중력 후')
        board = rotate_board()
        for i in range(N):
            print(*board[i], '회전 후')
        active_gravity()
        for i in range(N):
            print(*board[i], '중력 후')
        print('===========')
    return score


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(game())
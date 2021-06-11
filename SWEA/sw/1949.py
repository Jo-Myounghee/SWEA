'''
1
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
'''
def main():
    def find_start():
        start_lst = []
        for y in range(N):
            for x in range(N):
                if board[y][x] == max_height:
                    start_lst.append((x, y))
        return start_lst

    def move(x, y, cut, cnt):
        global answer, board
        if cnt >= 21:
            answer = max(cnt, answer)
            return
        # 오른쪽 아래 왼쪽 위
        dx = (1, 0, -1, 0)
        dy = (0, 1, 0, -1)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and not visited[ty][tx]:
                if board[ty][tx] < board[y][x]:
                    visited[ty][tx] = True
                    move(tx, ty, cut, cnt + 1)
                    visited[ty][tx] = False
                elif board[ty][tx] >= board[y][x] and not cut:
                    for k in range(1, K+1):
                        if board[ty][tx] - k < board[y][x]:
                            visited[ty][tx] = True
                            board[ty][tx] -= k
                            move(tx, ty, True, cnt + 1)
                            board[ty][tx] += k
                            visited[ty][tx] = False
        if cnt > answer:
            answer = cnt

    starts = find_start()
    for i in range(len(starts)):
        sx, sy = starts[i][0], starts[i][1]
        visited = [[False] * N for _ in range(N)]
        visited[sy][sx] = True
        move(sx, sy, False, 1)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0
    for i in range(N):
        max_height = max(max_height, max(board[i]))
    answer = 0
    main()
    print('#{} {}'.format(tc, answer))
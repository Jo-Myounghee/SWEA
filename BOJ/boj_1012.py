import sys
sys.setrecursionlimit(2503)

def dfs(x, y):
    global M, N

    board[y][x] = 0

    for i in range(4):
        tx = x + dir[i][0]
        ty = y + dir[i][1]

        if 0<=tx<M and 0<=ty<N and board[ty][tx] == 1:
            dfs(tx, ty)

    return True

T = int(input())
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for tc in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                if dfs(x, y):
                    cnt += 1

    print(cnt)
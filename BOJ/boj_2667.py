N = int(input())
board = [list(map(int, input())) for _ in range(N)]

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

answer = []
cnt = 0

def dfs(x, y):
    global cnt

    board[y][x] = 0
    cnt += 1

    for i in range(4):
        tx = x + dir[i][0]
        ty = y + dir[i][1]
        if 0 <= tx < N and 0 <= ty < N and board[ty][tx] == 1:
            dfs(tx, ty)
    return

for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            dfs(x, y)
            answer.append(cnt)
            cnt = 0

print(len(answer), *sorted(answer), sep="\n")
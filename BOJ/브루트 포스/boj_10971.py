def dfs(start, next, value, cnt):
    global min_val, visited

    if cnt == N:
        if board[next][start] != 0:
            min_val = min(min_val, value + board[next][start])
        return

    for i in range(N):
        if board[next][i] != 0 and i != start and not visited[i]:
            visited[i] = True
            dfs(start, i, value + board[next][i], cnt + 1)
            visited[i] = False


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_val = 1e9
for i in range(N):
    dfs(i, i, 0, 1)
print(min_val)
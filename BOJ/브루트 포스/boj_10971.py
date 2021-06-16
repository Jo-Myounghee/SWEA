def dfs(start, next, value, visited):
    global min_val

    if len(visited) == N:
        if board[next][start] != 0:
            min_val = min(min_val, value + board[next][start])
        return

    for i in range(N):
        if board[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + board[next][i], visited)
            visited.pop()


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min_val = 1e9
for i in range(N):
    dfs(i, i, 0, [i])
print(min_val)
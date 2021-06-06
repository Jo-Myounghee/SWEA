from collections import deque


def func(height):
    global N, board
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and board[y][x] > height:
                visited[y][x] = True
                visited = bfs(x, y, visited, height)
                cnt += 1
    return cnt

def bfs(sx, sy, visited, height):
    global N
    land = deque()
    land.append((sx, sy))
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    while land:
        nx, ny = land.popleft()
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if 0 <= tx < N and 0 <= ty < N and not visited[ty][tx]:
                visited[ty][tx] = True
                if board[ty][tx] > height:
                    land.append((tx, ty))
    return visited


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
max_val = 0
min_val = 1e9
for i in range(N):
    max_val = max(max_val, max(board[i]))
    min_val = min(min_val, min(board[i]))

for rain_height in range(max(min_val-1, 0), max_val+1):
    answer = max(answer, func(rain_height))
print(answer)
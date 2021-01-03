from collections import deque
import sys; sys.stdin = open('152input.txt', 'r')

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if (nx < 0 or ny < 0 or nx >= M or ny >= N) or board[ny][nx] == 0:
                continue
            if board[ny][nx] == 1:
                board[ny][nx] = board[y][x] + 1
                queue.append((nx, ny))
    return board[N-1][M-1]

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

print(bfs(0, 0))




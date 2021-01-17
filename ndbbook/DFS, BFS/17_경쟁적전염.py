# BFS
# 시작이 (1, 1)이고 맨 오른쪽 맨 아래가 (N, N)임
from collections import deque

N, K = map(int, input().split())
board = []
data = []
for y in range(N):
    board.append(list(map(int, input().split())))
    for x in range(N):
        if board[y][x] != 0:
            data.append((board[y][x], 0, x, y))
S, X, Y = map(int, input().split())

data.sort()
q = deque(data)

s = 0
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
    virus, s, x, y = q.popleft()
    if s == S:
        break

    for i in range(4):
        next_x = x + dir[i][0]
        next_y = y + dir[i][1]
        if 0 <= next_x < N and 0 <= next_y < N and board[next_y][next_x] == 0:
            board[next_y][next_x] = virus
            q.append((virus, s+1, next_x, next_y))

print(board[X-1][Y-1])



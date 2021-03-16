from collections import deque

def bfs():
    global w, h, cnt
    q = deque()
    q.append((0, 0))
    visited = [[False] * w for _ in range(h)]
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(dir)):
            tx = x + dir[i][0]
            ty = y + dir[i][1]
            if 0 <= tx < w and 0 <= ty < h and not visited[ty][tx]:
                visited[ty][tx] = True

                if board[ty][tx] == 0:
                    q.append((tx, ty))
                else:
                    cnt += 1
                    board[ty][tx] = 0
    return

h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
time = 0
cnt = 0
answer = [[0]*w for _ in range(h)]
while answer != board:
    time += 1
    bfs()

print(time, cnt, sep="\n")


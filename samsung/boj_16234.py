from collections import deque

def isBoard(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def BFS(_x, _y):
    global visited, L, R, board, isChange
    q = deque()
    q.append((_x, _y))
    group = deque()
    group.append((_x, _y))

    while q:
        x, y = q.pop()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if isBoard(tx, ty) and not visited[ty][tx] and L <= abs(board[y][x] - board[ty][tx]) <= R:
                visited[ty][tx] = True
                group.append((tx, ty))
                q.append((tx, ty))

    if len(group) > 1:
        temp_sum = 0
        for i in range(len(group)):
            _x, _y = group[i][0], group[i][1]
            temp_sum += board[_y][_x]
        avg = temp_sum // len(group)
        for _ in range(len(group)):
            _x, _y = group.popleft()
            board[_y][_x] = avg
        isChange = True


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
cnt = 0

while True:
    visited = [[False]*N for _ in range(N)]
    isChange = False
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                visited[y][x] = True
                BFS(x, y)
    if not isChange:
        break
    else:
        cnt += 1

print(cnt)
from collections import deque

def BFS(x, y, d):
    q = deque()
    q.append((x, y, d))
    road = deque()
    road.append((x, y))
    while q:
        x, y, d = q.popleft()
        visited[y][x] = True
        if isExit[y][x] == 1:
            while road:
                x, y = road.popleft()
                isExit[y][x] = 1
            return True
        elif isExit[y][x] == -1:
            while road:
                x, y = road.popleft()
                isExit[y][x] = -1
            return False

        tx = x + dir[d][0]
        ty = y + dir[d][1]

        if 0 <= tx < M and 0 <= ty < N:
            # print(tx, ty, 'tx, ty')
            if not visited[ty][tx]:
                q.append((tx, ty, board[ty][tx]))
                road.append((tx, ty))

            else:
                while road:
                    x, y = road.popleft()
                    isExit[y][x] = -1
                return False
        else:
            while road:
                x, y = road.popleft()
                isExit[y][x] = 1
            return True
    while road:
        x, y = road.popleft()
        isExit[y][x] = -1
    return False

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
isExit = [[0]*M for _ in range(N)]

dir = {'U': [0, -1], 'R': [1, 0], 'D': [0, 1], 'L': [-1, 0]}

cnt = 0
for y in range(N):
    for x in range(M):
        visited = [[False]*M for _ in range(N)]
        if isExit[y][x] == 1:
            cnt += 1
        elif isExit[y][x] == -1:
            continue
        elif BFS(x, y, board[y][x]):
            cnt += 1
        # print('-----------------------', x, y, 'x y --------------')

print(cnt)
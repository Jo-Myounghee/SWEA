def path(x, y):
    if x>=0 and x<N and y>=0 and y<N and board[y][x] != 1:
        return True
    return False

def DFS(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0

        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    return False


    global result

    if graph[y][x] == 1:
        result = 1
        return

    visited.append((x, y))
    for dir in range(4):
        testX = x + dx[dir]
        testY = y + dy[dir]
        if path(testX, testY) and (testX, testY) not in visited:
            DFS(testX, testY)

N, M = map(int, input().split())    # N개의 행, M개의 열 (0<=y<N, 0<=x<M)

graph = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[j][i] == 2:
            startX = i
            startY = j

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = []
result = 0
DFS(startX, startY)
print('#{} {}'.format(tc, result))

# test_case
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
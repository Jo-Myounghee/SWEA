'''
5 6
101010
111111
000001
111111
111111
'''
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = []

def bfs(x, y):
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= M or ty < 0 or ty >= N:
                continue
            if graph[ty][tx] == 0:
                continue
            if graph[ty][tx] == 1:
                graph[ty][tx] = graph[y][x] + 1
                queue.append((tx, ty))
    return graph[N-1][M-1]
print(bfs(0, 0))
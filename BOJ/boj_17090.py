import sys
sys.setrecursionlimit(10**9)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return True

    if board[y][x] == 'true':
        return True
    elif board[y][x] == 'false':
        return False

    if visited[y][x]:
        return False
    else:
        visited[y][x] = True
        dx, dy = dir[board[y][x]]
        tx = x + dx
        ty = y + dy

        result = dfs(tx, ty)
        board[y][x] = ('true' if result else 'false')
        return result

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dir = {'U': [0, -1], 'R': [1, 0], 'D': [0, 1], 'L': [-1, 0]}

cnt = 0
for y in range(N):
    for x in range(M):
        if dfs(x, y):
            cnt += 1

print(cnt)
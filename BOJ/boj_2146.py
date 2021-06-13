from collections import deque


def is_land(ix, iy):
    global N
    if 0 <= ix < N and 0 <= iy < N:
        return True
    return False


def numbering(ix, iy):
    global board, N, lands, visited
    temp_lands = [(ix, iy)]
    q = deque()
    q.append((ix, iy))
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        _x, _y = q.popleft()
        is_end = False
        for i in range(4):
            tx, ty = _x + dir[i][0], _y + dir[i][1]
            if is_land(tx, ty) and not visited[ty][tx]:
                if board[ty][tx] == 1:
                    q.append((tx, ty))
                if board[ty][tx] == 0 and not is_end:
                    is_end = True
                    temp_lands.append((_x, _y))
                visited[ty][tx] = True
    return temp_lands


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
lands = []
answer = N*N


for y in range(N):
    for x in range(N):
        if not visited[y][x] and board[y][x] == 1:
            temp = numbering(x, y)
            lands.append(temp)
        visited[y][x] = True


for i in range(len(lands)-1):
    land = lands[i]
    for j in range(i+1, len(lands)):
        another_land = lands[j]
        for k in range(len(land)):
            for t in range(len(another_land)):
                answer = min(answer, abs(land[k][0]-another_land[t][0])+abs(land[k][1]-another_land[t][1]))

print(answer-1)
def isRoad(x, y):
    if 0 <= x < M and 0 <= y < N:
        return True
    return False

def virus(x, y):
    global dx, dy
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isRoad(nx, ny):
            if temp[ny][nx] == 0:
                temp[ny][nx] = 2
                virus(nx, ny)

# 안전영역 크기 계산
def get_score():
    score = 0
    for y in range(N):
        for x in range(M):
            if temp[y][x] == 0:
                score += 1
    return score

def dfs(count):
    global result, N, M
    if count == 3:
        # board를 temp로 복제
        for y in range(N):
            for x in range(M):
                temp[y][x] = board[y][x]

        # 각 바이러스의 위치에서 전파 진행
        for y in range(N):
            for x in range(M):
                if temp[y][x] == 2:
                    virus(x, y)

        result = max(result, get_score())
        return

    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                board[y][x] = 1
                count += 1
                dfs(count)
                board[y][x] = 0
                count -= 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp = [[0]*M for _ in range(N)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
result = 0

dfs(0)
print(result)

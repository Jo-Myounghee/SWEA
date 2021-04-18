def isBoard(x, y):
    if x < 0 or x >= M or y < 0 or y >= N or board[y][x] == 6:
        return False
    return True

def watch(x, y, k):
    cnt = 0
    x, y = x+dx[k], y+dy[k]
    while isBoard(x, y):
        if not visited[y][x]:
            visited[y][x] = True
            cnt += 1
        x, y = x + dx[k], y + dy[k]
    return cnt

def cctv(x, y, type, k):
    cnt = 0
    if type == 1:
        cnt += watch(x, y, k)
    elif type == 2:
        cnt += watch(x, y, k)
        cnt += watch(x, y, (k+2)%4)
    elif type == 3:
        cnt += watch(x, y, k)
        cnt += watch(x, y, (k+1)%4)
    elif type == 4:
        cnt += watch(x, y, k)
        cnt += watch(x, y, (k+1)%4)
        cnt += watch(x, y, (k+2)%4)
    elif type == 5:
        for k in range(4):
            cnt += watch(x, y, k)
    return cnt

def solve(n, cnt):
    global ans, visited
    if ans == 0:
        return

    if n == len(cctv_lst):
        ans = min(ans, cnt)

    else:
        cx, cy, ct = cctv_lst[n]
        temp_visited = [visited[i][:] for i in range(N)]
        for k in range(4):
            solve(n+1, cnt-cctv(cx, cy, ct, k))
            visited = [temp_visited[i][:] for i in range(N)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv_lst = []
visited = [[False]*M for _ in range(N)]
ans = N*M
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

for y in range(N):
    for x in range(M):
        if board[y][x] == 5:
            if not visited[y][x]:
                visited[y][x] = True
                ans -= 1
            ans -= cctv(x, y, 5, 0)
        elif board[y][x] == 6:
            visited[y][x] = True
            ans -= 1
        elif board[y][x] != 0 and board[y][x] != 6:
            cctv_lst.append([x, y, board[y][x]])
            if not visited[y][x]:
                visited[y][x] = True
                ans -= 1

solve(0, ans)
print(ans)

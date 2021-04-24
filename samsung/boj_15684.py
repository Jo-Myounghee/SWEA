def check():
    for x in range(N):
        s = x
        for y in range(H):
            if board[y][s]:
                s += 1
            elif s > 0 and board[y][s-1]:
                s -= 1
        if s != x:
            return False
    return True

def solve(cnt, x, y):
    global ans
    if ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for _y in range(y, H):
        k = x if _y == y else 0
        for _x in range(k, N-1):
            if board[_y][_x]:
                _x += 1
            else:
                board[_y][_x] = 1
                solve(cnt+1, _x+1, _y)
                board[_y][_x] = 0

N, M, H = map(int, input().split())
board = [[0]*N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
ans = 4
solve(0, 0, 0)
print(ans if ans < 4 else -1)
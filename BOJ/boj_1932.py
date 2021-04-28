N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = [[0]*N for _ in range(N)]
ans[0][0] = board[0][0]

for y in range(1, N):
    for x in range(y+1):
        if x > 0:
            ans[y][x] = max(ans[y-1][x-1], ans[y-1][x]) + board[y][x]
        else:
            ans[y][x] = ans[y-1][x] + board[y][x]

print(max(ans[N-1]))
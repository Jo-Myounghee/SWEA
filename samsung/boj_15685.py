N = int(input())
board = [[0]*101 for _ in range(101)]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
v = [0]
ans = 0

for i in range(1, 11):
    k = 1<<(i-1)
    for j in range(k):
        v.append((v[k-j-1]+1)%4)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1
    for i in range(1<<g):
        x, y = x+dx[(v[i]+d)%4], y+dy[(v[i]+d)%4]
        board[y][x] = 1

for y in range(100):
    for x in range(100):
        if board[y][x] and board[y+1][x] and board[y][x+1] and board[y+1][x+1]:
            ans += 1

print(ans)
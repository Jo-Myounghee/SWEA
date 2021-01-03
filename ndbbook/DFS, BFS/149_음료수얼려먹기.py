import sys
# sys.stdin = open('149input.txt', 'r')
sys.stdin = open('149input1.txt', 'r')

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if board[y][x] == 0:
        board[y][x] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

cnt = 0
for j in range(N): # y
    for i in range(M): #x
        if dfs(i, j):
            cnt += 1

print(cnt)
import sys


def solution():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    _big = dp[x2][y2]
    _small = dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]
    return _big-_small


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

for y in range(N):
    for x in range(N):
        dp[y+1][x+1] = dp[y][x+1] + dp[y+1][x] - dp[y][x] + board[y][x]

for _ in range(M):
    print(solution())
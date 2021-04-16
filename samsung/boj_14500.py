def isRoad(x, y):
    global N, M
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    return True

def findSum(x, y):
    global board, ans
    max_total = 0
    for i in range(len(blocks)):
        temp_sum = board[y][x]
        for (dx, dy) in blocks[i]:
            tx, ty = x + dx, y + dy
            if isRoad(tx, ty):
                temp_sum += board[ty][tx]
        max_total = max(temp_sum, max_total)

    if max_total > ans:
        ans = max_total

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
blocks = (
    ((1, 0), (2, 0), (3, 0)),
    ((0, 1), (0, 2), (0, 3)),

    ((0, 1), (1, 0), (1, 1)),

    ((0, 1), (0, 2), (1, 2)),
    ((1, 0), (1, -1), (1, -2)),
    ((1, 0), (2, 0), (2, -1)),
    ((0, 1), (1, 1), (2, 1)),
    ((1, 0), (1, 1), (1, 2)),
    ((1, 0), (0, 1), (0, 2)),
    ((1, 0), (2, 0), (0, 1)),
    ((1, 0), (2, 0), (2, 1)),

    ((0, 1), (1, 1), (1, 2)),
    ((0, 1), (1, 0), (-1, 1)),
    ((1, 0), (1, -1), (0, 1)),
    ((1, 0), (1, 1), (2, 1)),

    ((1, 0), (2, 0), (1, 1)),
    ((0, 1), (1, 1), (0, 2)),
    ((1, -1), (1, 0), (2, 0)),
    ((1, 0), (1, -1), (1, 1))
)
ans = 0

for y in range(N):
    for x in range(M):
        findSum(x, y)

print(ans)
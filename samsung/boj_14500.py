def isRoad(x, y):
    global N, M
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    return True

def findSum(x, y):
    global board, visited, ans
    max_total = 0
    # 1-1 (오른쪽으로 4개)
    if isRoad(x+3, y):
        temp_total = sum(board[y][x:x+4])
        max_total = max(temp_total, max_total)
    # 1-2 (아래쪽으로 4개)
    if isRoad(x, y+3):
        temp_total = board[y][x] + board[y+1][x] + board[y+2][x] + board[y+3][x]
        max_total = max(temp_total, max_total)

    # 2-1 (오른쪽 한개, 아래쪽 한개, 오른쪽 아래 1개)
    if isRoad(x+1, y+1):
        temp_total = sum(board[y][x:x+2]) + sum(board[y+1][x:x+2])
        max_total = max(temp_total, max_total)

    # 3-1 (ㄴ모양)
    if isRoad(x+1, y+2):
        temp_total = board[y][x] + board[y+1][x] + board[y+2][x] + board[y+2][x+1]
        max_total = max(temp_total, max_total)

    # 3-2 (ㅢ 모양)
    if isRoad(x+2, y-1):
        temp_total = sum(board[y][x:x+3]) + board[y-1][x+2]
        max_total = max(temp_total, max_total)

    # 3-3 (ㄱ 모양)
    if isRoad(x + 1, y + 2):
        temp_total = sum(board[y][x:x + 2]) + board[y + 1][x + 1] + board[y + 2][x + 1]
        max_total = max(temp_total, max_total)

    # 3-4 (ㅣㅡ 모양)
    if isRoad(x+2, y) and isRoad(x, y+1):
        temp_total = sum(board[y][x:x+3]) + board[y+1][x]
        max_total = max(temp_total, max_total)

    # 3-1 대칭
    if isRoad(x+1, y-2):
        temp_total = sum(board[y][x:x+2]) + board[y-1][x+1] + board[y-2][x+1]
        max_total = max(temp_total, max_total)
    # 3-2 대칭
    if isRoad(x+2, y+1):
        temp_total = board[y][x] + sum(board[y+1][x:x+3])
        max_total = max(temp_total, max_total)
    # 3-3 대칭
    if isRoad(x+1, y) and isRoad(x, y+2):
        temp_total = sum(board[y][x:x+2]) + board[y+1][x] + board[y+2][x]
        max_total = max(temp_total, max_total)
    # 3-4 대칭
    if isRoad(x+2, y+1):
        temp_total = sum(board[y][x:x+3]) + board[y+1][x+2]
        max_total = max(temp_total, max_total)

    # 4-1 (|-|모양)
    if isRoad(x+1, y+2):
        temp_total = board[y][x] + board[y+1][x] + board[y+1][x+1] + board[y+2][x+1]
        max_total = max(temp_total, max_total)

    # 4-2 (_|-모양)
    if isRoad(x+2, y-1):
        temp_total = sum(board[y][x:x+2]) + board[y-1][x+1] + board[y-1][x+2]
        max_total = max(temp_total, max_total)
    # 4-1 대칭
    if isRoad(x+1, y-2):
        temp_total = board[y][x] + sum(board[y-1][x:x+2]) + board[y-2][x+1]
        max_total = max(temp_total, max_total)
    # 4-2 대칭
    if isRoad(x+2, y+1):
        temp_total = sum(board[y][x:x+2]) + board[y+1][x+1] + board[y+1][x+2]
        max_total = max(temp_total, max_total)

    # 5-1 (ㅜ 모양)
    if isRoad(x+2, y) and isRoad(x+1, y+1):
        temp_total = sum(board[y][x:x+3]) + board[y+1][x+1]
        max_total = max(temp_total, max_total)

    # 5-2 (ㅏ모양)
    if isRoad(x+1, y+1) and isRoad(x, y+2):
        temp_total = board[y][x] + sum(board[y+1][x:x+2]) + board[y+2][x]
        max_total = max(temp_total, max_total)

    # 5-3 (ㅗ모양)
    if isRoad(x+2, y) and isRoad(x+1, y-1):
        temp_total = sum(board[y][x:x+3]) + board[y-1][x+1]
        max_total = max(temp_total, max_total)

    # 5-4 (ㅓ모양)
    if isRoad(x+1, y-1) and isRoad(x+1, y+1):
        temp_total = sum(board[y][x:x+2]) + board[y-1][x+1] + board[y+1][x+1]
        max_total = max(temp_total, max_total)

    if max_total > ans:
        ans = max_total

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0

for y in range(N):
    for x in range(M):
        findSum(x, y)

print(ans)
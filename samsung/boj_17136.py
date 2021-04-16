def isok(nowr, nowc, size):
    for r in range(nowr, nowr + size):
        for c in range(nowc, nowc + size):
            if (not ((0 <= r < 10) and (0 <= c < 10))):
                return False
            if board[r][c] == 0:
                return False
    return True

def attach(nowr, nowc, size, tf):
    for r in range(nowr, nowr + size):
        for c in range(nowc, nowc + size):
            board[r][c] = tf

def isfinish():
    if sum(sum(board[i]) for i in range(10)) == 0:
        return True
    else:
        return False

def solve(index, cnt):
    global minAns

    if index >= 100:
        minAns = min(cnt, minAns)
        return

    if cnt >= minAns:
        return

    nowr = index // 10
    nowc = index % 10
    maxSize = 0

    for size in reversed(range(1, 6)):
        if isok(nowr, nowc, size):
            maxSize = size
            break
    if board[nowr][nowc] == 1:
        for size in reversed(range(1, maxSize+1)):
            if papers[size] > 0:
                attach(nowr, nowc, size, 0)
                papers[size] -= 1
                solve(index+1, cnt+1)
                papers[size] += 1
                attach(nowr, nowc, size, 1)
    else:
        solve(index+1, cnt)

minAns = 1e9
papers = [-1, 5, 5, 5, 5, 5]
board = [list(map(int, input().split())) for _ in range(10)]
solve(0, 0)
print(minAns if minAns < 1e9 else -1)
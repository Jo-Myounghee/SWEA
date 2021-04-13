def dfs(x, y, visited):
    dx, dy = dir[board[y][x]]
    tx = x + dx
    ty = y + dy
    visited.append((x, y))
    if tx < 0 or tx >= M or ty < 0 or ty >= N:
        for i in range(len(visited)):
            rx, ry = visited[i]
            isExit[ry][rx] = 1
        return True

    else:
        if (tx, ty) in visited:
            for i in range(len(visited)):
                rx, ry = visited[i]
                isExit[ry][rx] = 2
            return False
        else:
            ans = dfs(tx, ty, visited)
    return ans


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
isExit = [[0]*M for _ in range(N)]
dir = {'U': [0, -1], 'R': [1, 0], 'D': [0, 1], 'L': [-1, 0]}

cnt = 0
for y in range(N):
    for x in range(M):
        if isExit[y][x] == 1:
            cnt += 1
        elif isExit[y][x] == 2:
            continue
        else:
            ans = dfs(x, y, [])
            if ans == True:
                cnt += 1

print(cnt)
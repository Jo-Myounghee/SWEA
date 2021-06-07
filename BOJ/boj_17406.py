from collections import deque


def rotate(r, c, s):
    global temp_board
    q = deque()
    cnt = 0
    width = (2*s) + 1
    height = (2*s) + 1
    nx, ny = (c-s-1, r-s-1)
    while cnt < s:
        for i in range(width-1):
            q.append(temp_board[ny][nx+i])
        for i in range(height-1):
            q.append(temp_board[ny+i][nx+width-1])
        for i in range(width-1):
            q.append(temp_board[ny+height-1][nx+width-1-i])
        for i in range(height-1):
            q.append(temp_board[ny+height-1-i][nx])
        q.rotate(1)
        for i in range(width-1):
            temp_board[ny][nx+i] = q.popleft()
        for i in range(height-1):
            temp_board[ny+i][nx+width-1] = q.popleft()
        for i in range(width-1):
            temp_board[ny+height-1][nx+width-1-i] = q.popleft()
        for i in range(height-1):
            temp_board[ny+height-1-i][nx] = q.popleft()
        nx += 1
        ny += 1
        width -= 2
        height -= 2
        cnt += 1
    return


def perm(cnt):
    global arr_order, temp_order, visited
    if cnt == K:
        arr_order.append(temp_order[:])
        return

    for i in range(K):
        if not visited[i]:
            visited[i] = True
            temp_order.append(inputs[i])
            perm(cnt+1)
            visited[i] = False
            temp_order.pop()

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
inputs = [list(map(int, input().split())) for _ in range(K)]

arr_order = []
temp_order = []
visited = [False] * K
perm(0)

answer = 1e9
for i in range(len(arr_order)):
    temp_board = [board[i][:] for i in range(N)]
    for j in range(K):
        rotate(arr_order[i][j][0], arr_order[i][j][1], arr_order[i][j][2])
    for j in range(N):
        answer = min(answer, sum(temp_board[j]))

print(answer)
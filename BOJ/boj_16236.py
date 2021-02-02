from collections import deque

def bfs(x, y):
    global N
    dir = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    q = deque()
    q.append((x, y, 0))

    eatq = deque()

    eat_time = 0
    eat_num = 0

    level = 2

    min_x = x
    min_y = y

    while True:
        eat = False
        visited = [[False] * N for _ in range(N)]
        visited[min_y][min_x] = True
        while q:
            now_x, now_y, cnt = q.popleft()
            if board[now_y][now_x] == 9:
                board[now_y][now_x] = 0

            if board[now_y][now_x] != 0 and board[now_y][now_x] < level:
                eat = True
                eatq.append((now_x, now_y, cnt))
                while q:
                    test_x, test_y, cnt = q.popleft()
                    if board[test_y][test_x] != 0 and board[test_y][test_x] < level:
                        eatq.append((test_x, test_y, cnt))
            else:
                for i in range(4):
                    test_x = now_x + dir[i][0]
                    test_y = now_y + dir[i][1]
                    if 0 <= test_x < N and 0 <= test_y < N and visited[test_y][test_x] == False and board[test_y][test_x] <= level:
                        visited[test_y][test_x] = True
                        q.append((test_x, test_y, cnt+1))

        if not eat:
            break

        min_x = -1
        min_y = -1
        min_cnt = 1e9

        while eatq:
            eat_x, eat_y, eat_cnt = eatq.popleft()
            if eat_cnt < min_cnt:
                min_cnt = eat_cnt
                min_x = eat_x
                min_y = eat_y

            elif eat_cnt == min_cnt:
                if eat_y < min_y:
                    min_cnt = eat_cnt
                    min_x = eat_x
                    min_y = eat_y

                elif eat_y == min_y:
                    if eat_x < min_x:
                        min_cnt = eat_cnt
                        min_x = eat_x
                        min_y = eat_y

        if min_x != -1:
            board[min_y][min_x] = 0
            eat_time += min_cnt
            eat_num += 1
            if eat_num == level:
                eat_num = 0
                level += 1
            q.append((min_x, min_y, 0))

    return eat_time

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for y in range(N):
    for x in range(N):
        if board[y][x] == 9:
            start_x, start_y = x, y

print(bfs(start_x, start_y))

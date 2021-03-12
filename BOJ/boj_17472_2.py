'''
10 6
0 0 0 1 0 0
0 0 0 1 0 0
0 1 0 0 0 1
0 0 0 0 0 0
1 1 0 1 1 0
1 0 0 0 1 0
1 1 0 0 1 0
0 0 0 0 1 1
0 0 0 0 0 0
0 1 0 0 0 0
'''
def col_ok(x, y1, y2):
    start, goal = min(y1, y2), max(y1, y2)
    if goal - start <= 2:
        return 1000
    for i in range(start+1, goal):
        if board[i][x] != 0:
            return 1000
    return goal-start-1

def row_ok(y, x1, x2):
    start, goal = min(x1, x2), max(x1, x2)
    if goal - start <= 2:
        return 1000
    for i in range(start+1, goal):
        if board[y][i] != 0:
            return 1000
    return goal-start-1

def island_dist(start, goal):
    dist = 1000
    for i in range(len(words_location[start])):
        start_x, start_y = words_location[start][i][0], words_location[start][i][1] 
        for j in range(len(words_location[goal])):
            goal_x, goal_y = words_location[goal][j][0], words_location[goal][j][1] 
            if start_x == goal_x:
                temp = col_ok(start_x, start_y, goal_y)
                if temp < dist:
                    dist = temp
            elif start_y == goal_y:
                temp = row_ok(start_y, start_x, goal_x)
                if temp < dist:
                    dist = temp
    island_dist_lst.append((dist, start, goal))

def comb(cnt, start):
    global island_len
    if cnt == 2:
        island_dist(answer[0], answer[1])
        return
    else:
        for i in range(start, island_len):
            answer.append(i)
            comb(cnt+1, i+1)
            answer.pop()

def dfs(x, y, word):
    board[y][x] = word
    words_location[word-11].append((x, y))

    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i in range(len(dir)):
        tx = x + dir[i][0]
        ty = y + dir[i][1]
        
        if 0 <= tx < M and 0 <= ty < N:
            if board[ty][tx] == 1:
                dfs(tx, ty, word)

# 섬이 연결되어있나
# def isConnect(f1, f2):


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

words = [11, 12, 13, 14, 15, 16]
words_location = [[] for _ in range(6)]
island_dist_lst = []

island_len = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            dfs(x, y, words[island_len])
            island_len += 1
answer = []
comb(0, 0)

island_dist_lst.sort()

# prim 사용하기 ..

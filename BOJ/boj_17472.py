# 섬의 거리
# 만약 최소 값이 1이면 ㄴㄴ
# 일자로 이어지지 않는다면 100
# (거리, 섬1, 섬2) 이렇게 island_dist_lst에 담기
def col_ok(x, y1, y2):
    start, goal = min(y1, y2), max(y1, y2)
    if goal - start <= 2:
        return 100
    for i in range(start+1, goal):
        if board[i][x] != 0:
            return 100
    return goal-start-1

def row_ok(y, x1, x2):
    start, goal = min(x1, x2), max(x1, x2)
    if goal - start <= 2:
        return 100
    for i in range(start+1, goal):
        if board[y][i] != 0:
            return 100
    return goal-start-1

def island_dist(start, goal):
    dist = 100
    for i in range(len(words_location[start])):
        start_x, start_y = words_location[start][i][0], words_location[start][i][1] 
        for j in range(len(words_location[goal])):
            goal_x, goal_y = words_location[goal][j][0], words_location[goal][j][1] 
            # x좌표가 같다면
            if start_x == goal_x:
                # 둘이 차이가 2이하이면 pass
                # 가운데 장애물은 없는지 확인
                temp = col_ok(start_x, start_y, goal_y)
                # 거리 값이 현재 dist보다 작다면 갱신
                if temp < dist:
                    dist = temp
            # y좌표가 같다면
            elif start_y == goal_y:
                # 둘이 차이가 2이하이면 pass
                # 가운데 장애물은 없는지 확인
                temp = row_ok(start_y, start_x, goal_x)
                # 거리 값이 현재 dist보다 작다면 갱신
                if temp < dist:
                    dist = temp
    island_dist_lst.append((dist, start, goal))

def comb(cnt, start):
    global island_len
    if cnt == 2:
        print(answer)
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

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 땅 영역 숫자 바꾸기
words = [11, 12, 13, 14, 15, 16]
words_location = [[] for _ in range(6)]
island_dist_lst = []
'''print(words_location)'''

island_len = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            dfs(x, y, words[island_len])
            island_len += 1
'''print(words_location)'''
# 2개만 뽑는 조합 list -> nC2
answer = []
comb(0, 0)

# 각각의 조합 (섬, 섬) 간의 최소 거리 구하기 -> 연결이 안되는 경우 100으로 넣기
# (거리, 섬1, 섬2) 이렇게 넣기 

# 최소 거리 (총 섬의 갯수 -1)개의 합 == ANS 
island_dist_lst.sort()
print(island_dist_lst)

total = 0
is_answer = True
for i in range(island_len-1):
    if island_dist_lst[i][0] == 100:
        print(-1)
        is_answer = False
        break
    total += island_dist_lst[i][0]

if is_answer:
    print(total)
# 


'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
from itertools import combinations

# for문 이용해서 DFS사용하기, visited 배열과 함께
def DFS(x, y):
    visited[y][x] = True
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(4):
        temp_x = dir[i][0] + x
        temp_y = dir[i][1] + y
        if 0 <= temp_x < M and 0 <= temp_y < N:
            if temp_board[temp_y][temp_x] != 1 and visited[temp_y][temp_x] == False:
                temp_board[temp_y][temp_x] = 2
                return DFS(temp_x, temp_y)
        continue

    return

N, M = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]
# 1. 0인 부분 위치를 모두 한 리스트에 담기
zero_lst = []
wall_len = 0


for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            zero_lst.append((x, y))
        elif board[y][x] == 1:
            wall_len += 1
print(wall_len, 'wall_len')
zero_num = len(zero_lst)
# 2. 리스트안에서 3개 뽑기 -> combination으로 구하기
wall_lst = list(combinations(zero_lst, 3))
total_safe = 0 # 바이러스 영역의 최소 크기
# 3. 각각의 경우(3개를 골랐을 때)에서 일어날 수 있는 안전영역 크기 구하기
for i in range(len(wall_lst)):
    visited = [[0] * M for _ in range(N)]
    temp_wall_lst = wall_lst[i]
    temp_safe = 0
    temp_board = [board[k][0:M] for k in range(len(board))]
    for j in range(3):
        x, y = temp_wall_lst[j][0], temp_wall_lst[j][1]
        temp_board[y][x] = 1

    for y in range(N):
        for x in range(M):
            if visited[y][x] == False and board[y][x] == 2:
                DFS(x, y)

    temp_safe = 0
    for y in range(N):
        for x in range(M):
            if temp_board[y][x] == 0:
                temp_safe += 1
        # print(visited[y])
    if temp_wall_lst == ((1, 0), (0, 1), (3, 5)):
        print('########')
        print(temp_safe)
    if temp_safe > total_safe:
        print(temp_safe)
        total_safe = temp_safe

print('yes') if board == temp_board else print('no')
print('total_safe')
print(total_safe)

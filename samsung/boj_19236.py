from copy import deepcopy
array = [[None]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기 번호, 방향]을 저장
        array[i][j] = [data[j*2], data[j*2+1]-1]

dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
# dir = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

result = 0

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = (direction+1)%8

def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y < 4 :
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result

    temp_array = deepcopy(array)
    print(temp_array)

    total += temp_array[now_x][now_y][0]
    temp_array[now_x][now_y][0] = -1

    move_all_fishes(temp_array, now_x, now_y)
    for i in range(len(temp_array)):
        print(temp_array[i])
    print(total, 'total')
    print('=============')

    positions = get_possible_positions(temp_array, now_x, now_y)
    if len(positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(temp_array, next_x, next_y, total)
    temp_array = [array[i][:] for i in range(len(array))]
print(array)
dfs(array, 0, 0, 0)
print(result)
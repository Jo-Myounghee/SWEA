# 배치한 경우 죽일 수 있는 적의 수
def dieEnemyNumbers():
    pass

# 3명 배치
# 적이 존재하는 경우 계속 진행 : while
def setDefence(lst):
    global N, M, D
    e = enemy[:]
    print(e, 'enemy')
    visited = [False] * len(e)
    temp_board = [0] * len(board)
    for i in range(len(board)):
        temp_board[i] = board[i][:]
    cnt = 0

    while e:
        # 죽일 적
        enemy_lst = []
        for i in range(len(lst)):
            # 각 궁수의 좌표
            x, y = defences[lst[i]][0], defences[lst[i]][1]
            print(x, y, '궁수')
            flag = False
            # 가까이서부터 적이 존재하는지 확인
            for j in range(1, D+1):
                dir = [[-1, 0], [0, 1], [0, -1], [1, 0]]
                for k in range(4):
                    tx = x + (dir[k][0]*j)
                    ty = y + (dir[k][1]*j)
                    if 0 <= tx < M and 0 <= ty < N and temp_board[ty][tx] == 1:
                        try:
                            enemy_lst.append((tx, ty))
                            print(visited)
                            visited[e.index((tx, ty))] = True
                            print('break의 범위는?')
                            flag = True
                            break
                        except:
                            continue
                if flag:
                    break
        # 죽이기
        for i in range(len(visited)):
            if visited[i]:
                e[i] = (-1, -1)
                cnt += 1
                print(cnt)

        # 적 아래로 내리기
        for i in range(len(e)):
            ex, ey = e.pop(0)
            temp_board[ey][ex] = 0
            if ex == -1 and ey == -1:
                pass
            elif ey + 1 >= N:
                pass
            else:
                e.append((ex, ey+1))
                temp_board[ey+1][ex] = 1

        visited = [False] * len(e)

    # return 죽인 적의 수
    return cnt

def comb(cnt, start):
    global max
    if cnt == 3:
        print('comb_lst', comb_lst)
        c = setDefence(comb_lst)
        if max < c:
            max = c
        return

    for i in range(start, len(defences)):
        comb_lst.append(i)
        comb(cnt+1, i+1)
        comb_lst.pop()

    return max


N, M, D = map(int, input().split())
board = []
enemy = []
comb_lst = []
defences = []
max = 0

for y in range(N):
    row = list(map(int, input().split()))
    for i in range(len(row)):
        if row[i] == 1:
            enemy.append((i, y))
        defences.append((i, y))
    board.append(row)

print(board)
print('defences', defences)
print(comb(0, 0), 'ans')
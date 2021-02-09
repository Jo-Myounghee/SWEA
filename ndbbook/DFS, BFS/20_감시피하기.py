def comb(lst, n):
    ret = []
    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])

    elif n > 1:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:], n-1):
                ret.append([lst[i]]+temp)
    return ret

def canblock(x, y):
    for i in range(len(teacher)):
        

N = int(input())
board = [list(map(input().split())) for _  in range(N)]
teacher = []
student = []
path = []

for y in range(N):
    for x in range(N):
        if board[y][x] == 'T':
            teacher.append((x, y))
        elif board[y][x] == 'S':
            student.append((x, y))
        else:
            path.append((x, y))

blocks = comb(path, 3)
ans = false
for i in range(len(blocks)):
    if ans:
        break
    now_blocks = blocks[i]
    for j in range(len(now_blocks)):
        x, y = now_blocks[j][0], now_blocks[j][1]
        board[y][x] = 'O'

        if canblock(0, 0):
            ans = 'yes'
            print(ans)
            break

    for j in range(len(now_blocks)):
        x, y = now_blocks[j][0], now_blocks[j][1]
        board[y][x] = 'X'

if not ans:
    print('NO')



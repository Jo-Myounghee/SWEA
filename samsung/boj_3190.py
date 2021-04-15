from collections import deque

def isEnd(x, y):
    global board
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    elif board[y][x] == True and board[y][x] != 'apple':
        return True
    return False

def move():
    global ans, now_dir
    while q:
        x, y = q[0]

        if bam_dirs and ans == int(bam_dirs[0][0]):
            now_dir = rotate(now_dir, bam_dirs[0][1])
            bam_dirs.pop(0)

        tx = x + dirs[now_dir][0]
        ty = y + dirs[now_dir][1]

        if not isEnd(tx, ty):
            if board[ty][tx] != 'apple':
                x, y = q.pop()
                board[y][x] = False
            q.appendleft((tx, ty))
            board[ty][tx] = True
        else:
            return
        ans += 1


def rotate(now_dir, direction):
    if direction == "D":
        return (now_dir + 1) % 4
    elif direction == 'L':
        return (now_dir-1) % 4


N = int(input())
K = int(input())
board = [[False]*N for _ in range(N)]
apples = [list(map(int, input().split())) for _ in range(K)]
for i in range(len(apples)):
    ay = apples[i][0] - 1
    ax = apples[i][1] - 1
    board[ay][ax] = 'apple'

L = int(input())
bam_dirs = [list(map(str, input().split())) for _ in range(L)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
now_dir = 0
ans = 0

q = deque()
q.append((0, 0))
board[0][0] = True

move()
print(ans+1)
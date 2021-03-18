def shoot(y, position, s_board):
    for d in range(1, D+1):
        for left in range(d, -1, -1):
            height = d - left
            if height > 0 and 0 <= y - height < N and 0 <= position - left < M and s_board[y-height][position - left] == 1:
                return (position - left, y - height)
        for right in range(1, d+1, 1):
            height = d - right
            if height > 0 and 0 <= y - height < N and 0 <= position + right < M and s_board[y - height][position + right] == 1:
                return (position + right, y - height)
    return None

def simulation(positions):
    s_board = [0] * len(board)
    for i in range(len(board)):
        s_board[i] = board[i][:]

    killed_amount = 0
    for y in range(N, 0, -1):
        killed = []
        for position in positions:
            killed_enemy = shoot(y, position, s_board)
            if killed_enemy is not None:
                killed.append(killed_enemy)
        for killed_enemy in killed:
            if s_board[killed_enemy[1]][killed_enemy[0]] == 1:
                s_board[killed_enemy[1]][killed_enemy[0]] = 0
                killed_amount += 1
    return killed_amount

N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            max_v = max(max_v, simulation((i, j, k)))

print(max_v)

# 3C2
def comb(cnt, start):
    if cnt == 3:
        print(answer)
        return

    for i in range(start, 3):
        answer.append(i)
        comb(cnt+1, i+1)
        answer.pop()

answer = []

# 3P2
def perm(k):
    global N, inputs, answer


    if k == N:
        print(answer)
        return

    for i in range(len(inputs)):
        if not visited[i]:
            visited[i] = True
            answer.append(inputs[i])
            perm(k + 1)
            visited[i] = False
            answer.pop()

N = 3
inputs = [1, 2, 3]
answer = []
visited = [False] * N
perm(0)


# 부분집합
def f(k, n):
    if n == k:  # b배열을 벗어나면
        for i in range(n):
            if b[i] == 1:
                print(A[i], end=' ')
        print()
    else:
        b[k] = 0
        f(k + 1, n)
        b[k] = 1
        f(k + 1, n)

A = [1, 2, 3]
b = [0, 0, 0]
f(0, 3)


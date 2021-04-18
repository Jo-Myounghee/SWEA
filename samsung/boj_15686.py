def solve(cnt, total):
    global minAns, chicken_group, homes
    if cnt == len(homes):
        minAns = min(minAns, total)
        return
    temp_dist = 1e9
    for i in range(M):
        temp_dist = min(temp_dist, abs(homes[cnt][0]-chicken_group[i][0]) + abs(homes[cnt][1]-chicken_group[i][1]))
    total += temp_dist
    solve(cnt+1, total)


def comb(cnt, start):
    global M
    if cnt == M:
        solve(0, 0)
        return

    for i in range(start, len(chickens)):
        chicken_group.append(chickens[i])
        comb(cnt+1, i+1)
        chicken_group.pop()

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
homes = []
chickens = []
minAns = 1e9

for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            homes.append((x, y))
        elif board[y][x] == 2:
            chickens.append((x, y))

chicken_group = []
comb(0, 0)
print(minAns)
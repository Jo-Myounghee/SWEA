N, M, K = map(int, input().split())
eats = [[5] * N for _ in range(N)]
add_eats = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for idx in range(K):
    for y in range(N):
        for x in range(N):
            if len(trees[y][x]) > 0:
                trees[y][x].sort()
                isDead = False
                for i in range(len(trees[y][x])):
                    if not isDead:
                        if eats[y][x] >= trees[y][x][i]:
                            eats[y][x] -= trees[y][x][i]
                            trees[y][x][i] += 1
                        else:
                            isDead = True
                            eats[y][x] += (trees[y][x][i] // 2)
                            trees[y][x][i] = 0
                    else:
                        eats[y][x] += (trees[y][x][i] // 2)
                        trees[y][x][i] = 0

    dir = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

    for y in range(N):
        for x in range(N):
            if len(trees[y][x]) > 0:
                trees[y][x].sort()
                while trees[y][x] and trees[y][x][0] == 0:
                    trees[y][x].pop(0)
                for i in range(len(trees[y][x])):
                    if trees[y][x][i] % 5 == 0:
                        for j in range(len(dir)):
                            tx = x + dir[j][0]
                            ty = y + dir[j][1]
                            if 0 <= tx < N and 0 <= ty < N:
                                trees[ty][tx].append(1)
    for y in range(N):
        for x in range(N):
            eats[y][x] += add_eats[y][x]

answer = 0
for y in range(N):
    for x in range(N):
        answer += len(trees[y][x])

print(answer)
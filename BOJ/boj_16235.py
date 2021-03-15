'''
10 10 1000
100 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1
2 2 1
3 3 1
4 4 1
5 5 1
6 6 1
7 7 1
8 8 1
9 9 1
10 10 1
'''
N, M, K = map(int, input().split()) # N : 땅의 크기 NXN // M : 나무의 개수
eats = [[5] * N for _ in range(N)] # 기존의 양분 양
add_eats = [list(map(int, input().split())) for _ in range(N)] # 겨울에 추가되는 양분의 양
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
# K년 후 나무의 개수 ?

for idx in range(K):
    # 봄, 여름
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
    # 가을
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

    # 겨울
    for y in range(N):
        for x in range(N):
            eats[y][x] += add_eats[y][x]

answer = 0
for y in range(N):
    for x in range(N):
        answer += len(trees[y][x])

print(answer)
# https://www.acmicpc.net/problem/15686

from itertools import combinations

N, M = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]

chickens = []
homes = []

for y in range(N):
    for x in range(N):
        if board[y][x] == 2:
            chickens.append((x, y))
        elif board[y][x] == 1:
            homes.append((x, y))

total_lst = [[N*N]*len(chickens) for _ in range(len(homes))]

chickenshop = list(combinations(chickens, M))

min_val = 1e9
for k in range(len(chickenshop)):
    chicken = chickenshop[k]
    temp = 0
    for y in range(len(homes)):
        for x in range(len(chicken)):
            total_lst[y][x] = abs(homes[y][0] - chicken[x][0]) + abs(homes[y][1] - chicken[x][1])
        temp += min(total_lst[y])
    if temp < min_val:
        min_val = temp

print(min_val)


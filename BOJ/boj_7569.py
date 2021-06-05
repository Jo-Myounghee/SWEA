from collections import deque
import sys


def grow_tomato():
    global ok_tomato, adj
    ok_tomato_len = len(ok_tomato)
    change_cnt = 0
    for _ in range(ok_tomato_len):
        nx, ny, nh = ok_tomato.popleft()
        for i in range(6):
            tx, ty, th = nx + adj[i][0], ny + adj[i][1], nh + adj[i][2]
            if 0 <= tx < M and 0 <= ty < N and 0 <= th < H and tomatoes[th][ty][tx] == 0:
                change_cnt += 1
                tomatoes[th][ty][tx] = 1
                ok_tomato.append((tx, ty, th))
    return change_cnt


M, N, H = map(int, sys.stdin.readline().split())
tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

ok_tomato = deque()
adj = [(0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
answer = 0
is_answer = False
yet_tomato = 0

for h in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[h][y][x] == 1:
                ok_tomato.append((x, y, h))
            elif tomatoes[h][y][x] == 0:
                yet_tomato += 1

while yet_tomato > 0:
    change_cnt = grow_tomato()
    yet_tomato -= change_cnt
    if change_cnt == 0 and yet_tomato > 0:
        is_answer = True
        print(-1)
        break
    answer += 1

if not is_answer:
    print(answer)
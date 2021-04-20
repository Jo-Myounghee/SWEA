from collections import deque

def comb(start, cnt):
    global M, minAns, virus_temp
    if cnt == M:
        ans = bfs(virus_temp)
        if ans != -1:
            minAns = min(minAns, ans)

    else:
        for i in range(start, len(viruses)):
            virus_temp.append(viruses[i])
            comb(i+1, cnt+1)
            virus_temp.pop()

def bfs(lst):
    global visited, virus_cnt_total
    virus_cnt = virus_cnt_total
    if virus_cnt == 0:
        return 0
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    temp_visited = [visited[i][:] for i in range(N)]
    q = deque()
    for i in range(len(lst)):
        _x, _y = lst[i]
        q.append((_x, _y, 1))
        # 처음 cnt 값은 1로 시작
        temp_visited[_y][_x] = 1
    while q:
        x, y, cnt = q.popleft()
        if cnt > minAns:
            return -1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if temp_visited[ty][tx] == 0 or temp_visited[ty][tx] == -2:
                    if temp_visited[ty][tx] == 0:
                        virus_cnt -= 1
                        if virus_cnt == 0:
                            return cnt
                    q.append((tx, ty, cnt+1))
                    temp_visited[ty][tx] = cnt+1
    if virus_cnt == 0:
        return cnt-1
    else:
        return -1

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
viruses = []
virus_temp = []
minAns = 1e9
virus_cnt_total = N*N

for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            visited[y][x] = -1
            virus_cnt_total -= 1
        elif board[y][x] == 2:
            visited[y][x] = -2
            viruses.append((x, y))
            virus_cnt_total -= 1
if virus_cnt_total > 0:
    comb(0, 0)
    if minAns == 1e9:
        minAns = -1
    print(minAns)
else:
    print(0)

'''
11 2
1 1 0 1 1 1 1 1 0 1 1
1 1 2 1 1 1 1 1 2 1 1
0 1 2 1 1 1 0 1 2 1 1
0 1 0 1 1 1 0 1 0 1 1
0 0 2 0 0 1 0 0 2 0 0
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
-> 4

5 3
2 2 2 0 0
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
-> 2

4 2
0 1 1 0
2 1 1 2
2 1 1 2
0 1 1 0
-> 2

5 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
2 0 0 2 0
1 1 1 1 1
-> 2

5 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
0 2 0 2 0
1 1 1 1 1
-> 3

5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 2 0
-> 1

4 1
2 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-> 0
'''
N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

def change(x, y):
    if x + 2 < M and y + 2 < N:
        for i in range(3):
            for j in range(3):
                if A[y+i][x+j] == 1:
                    A[y+i][x+j] = 0
                else:
                    A[y+i][x+j] = 1

cnt = 0
for y in range(N):
    for x in range(M):
        if A[y][x] != B[y][x]:
            change(x, y)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)
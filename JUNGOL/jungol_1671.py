N = int(input())

arr = [[0]*100 for _ in range(100)]

for i in range(N):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            arr[y+j][x+k] = 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

diag_dx = [1, 1, -1, -1]
diag_dy = [1, -1, 1, -1]

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[j][i]:
            for k in range(4):
                if arr[j+dy[k]][i+dx[k]] == 0:
                    cnt += 1
                    arr[j][i] = 2
                    break

for i in range(100):
    for j in range(100):
        if arr[j][i] == 1:
            for k in range(4):
                if arr[j+diag_dy[k]][i+diag_dx[k]] == 0:
                    cnt += 1
                    arr[j][i] = 2
                    break

print(cnt)
import sys

sys.stdin = open("./input_data/input_1979.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        number = list(map(int, input().split()))
        arr.append(number)
    cnt = 0
    for i in range(N):
        total_row = 0
        total_column = 0
        for j in range(N):
            if arr[i][j] == 1:
                total_row += 1
            else:
                if total_row == K:
                    cnt += 1
                total_row = 0
            if arr[j][i] == 1:
                total_column += 1
            else:
                if total_column == K:
                    cnt += 1
                total_column = 0
        if total_row == K:
            cnt += 1
        if total_column == K:
            cnt += 1
    print(f'#{tc} {cnt}')

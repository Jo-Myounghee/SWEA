import sys

sys.stdin = open("./input_data/input_2005.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*N for i in range(N)]

    for i in range(N):
        if i == 0:
            arr[i][0] = 1
        else:
            arr[i][0] = 1
            arr[i][i] = 1
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end = ' ')
        print()


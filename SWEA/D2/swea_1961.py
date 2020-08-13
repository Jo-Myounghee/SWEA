import sys

sys.stdin = open("./input_data/input_1961.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] for _ in range(N)]
    result = []
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    n = 0
    while n < 3: //여기를 N으로 함
        dst = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                dst[j][N-1-i] = arr[i][j]
        result.append(dst)
        arr = dst
        n += 1

    print(f'#{tc}')
    for i in range(N):
        for j in range(3): //여기를 N으로 함
            for k in range(N):
                print(result[j][i][k], end='')
            print(end=' ')
        print()

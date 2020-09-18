for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]

    total = 0
    for y in range(N):
        if y <= (N // 2):
            for x in range((N // 2) - y, (N // 2) + y + 1):
                total += lst[y][x]
        else:
            for x in range((N // 2 - (N - y - 1)), (N // 2 + (N - y - 1)) + 1):
                total += lst[y][x]

    print('#{} {}'.format(tc, total))
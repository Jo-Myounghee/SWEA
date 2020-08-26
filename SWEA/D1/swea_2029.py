T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    c, d = divmod(a, b)
    print(f'#{tc} {c} {d}')
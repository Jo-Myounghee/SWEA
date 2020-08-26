T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    if n > m:
        result = '>'
    elif n < m:
        result = '<'
    else:
        result = '='
    print(f'#{tc} {result}')
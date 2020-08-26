T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    max_num = max(numbers)
    print(f'#{tc} {max_num}')
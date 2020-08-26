T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    avg_num = round(sum(numbers) / len(numbers))
    print(f'#{tc} {avg_num}')
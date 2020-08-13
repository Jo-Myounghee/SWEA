import sys

sys.stdin = open("./input_data/input_1966.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    n = 0
    while n < N:
        for i in range(len(numbers)):
            if i > 0:
                if numbers[i-1] > numbers[i]:
                    temp = numbers[i-1]
                    numbers[i-1] = numbers[i]
                    numbers[i] = temp
        n += 1
    print(f'#{tc}', end = ' ')
    for i in numbers:
        print(i, end = ' ')
    print()




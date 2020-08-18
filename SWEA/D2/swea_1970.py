import sys

sys.stdin = open("./input_data/input_1970.txt", "r")

T = int(input())

for tc in range(1, T+1):
    money = int(input())
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    numbers = [0] * 8
    print(f'#{tc}')
    while money >= 10:
        for i in range(len(moneys)):
            numbers[i] = money // moneys[i]
            money = money % moneys[i]
            print(numbers[i], end=' ')
    print()
    


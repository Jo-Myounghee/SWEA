import sys

sys.stdin = open("./input_data/input(1948).txt", "r")

T = int(input())

for tc in range(1, T + 1):
    day_lst = list(map(int, input().split()))
    m1 = day_lst[0]
    d1 = day_lst[1]
    m2 = day_lst[2]
    d2 = day_lst[3]

    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = 0

    for i in range(m1 - 1, m2 - 1):
        total_day += day_list[i]

    result = total_day - d1 + d2 + 1

    print(f'#{tc} {result}')

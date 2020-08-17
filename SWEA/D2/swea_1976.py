import sys

sys.stdin = open("./input_data/input_1976.txt", "r")

T = int(input())

for tc in range(1, T+1):
    times = list(map(int, input().split()))

    min_tot = times[1] + times[3]
    h_tot = times[0] + times[2]

    if min_tot // 60 >= 1:
        h_tot += min_tot // 60
        min_tot -= (min_tot // 60) * 60 
    
    if h_tot // 12 >=1:
        h_tot %= 12
        if (h_tot % 12) == 0:
            h_tot = 12

    print(f'#{tc} {h_tot} {min_tot}')
    
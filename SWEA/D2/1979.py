import sys

sys.stdin = open("./input_data/input_1979.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    for _ in range(N):
        number = list(map(str, input().split()))
        str_num = ''
        for i in range(N):
            str_num+=number[i]
        cnt = 0
        if '1'*K in str_num:
            cnt += 1
    print(cnt)

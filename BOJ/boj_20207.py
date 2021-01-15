'''
7
2 4
4 5
5 6
5 7
7 9
11 12
12 12
'''
N = int(input())
dates = [list(map(int, input().split())) for _ in range(N)]

board = [0]*366

for i in range(len(dates)):
    start_date = dates[i][0]
    final_date = dates[i][1]
    n = start_date
    while n != final_date+1:
        board[n] += 1
        n += 1

max_val = 0
cnt = 0
ans = 0
for i in range(len(board)):
    if board[i]:
        cnt += 1
        if max_val < board[i]:
            max_val = board[i]

    elif not board[i] and cnt:
        ans += max_val * cnt
        cnt = 0
        max_val = 0

print(ans + (max_val*cnt))
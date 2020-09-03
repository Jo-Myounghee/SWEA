#
# N = int(input())
# board = [[0] * 101 for _ in range(101)]
#
# for num in range(1, N+1):
#     X, Y, xsize, ysize = map(int, input().split())
#     for dy in range(ysize):
#         for dx in range(xsize):
#             board[Y+dy][X+dx] = num
#
# for num in range(1, N+1):
#     SUM = 0
#     for y in range(101):
#         for x in range(101):
#             if board[y][x] == num:
#                 SUM += 1
#     print(SUM)
#

N = int(input())
board = [[0] * 101 for _ in range(101)]

for num in range(1, N+1):
    info = list(map(int, input().split()))
    for y in range(info[3]):
        for x in range(info[2]):
            board[info[1]+y][info[0]+x] = num

lst = [0]* (N+1)

for y in range(101):
    for x in range(101):
        if board[y][x] != 0:
            lst[board[y][x]] += 1

for i in range(1, N+1):
    print(lst[i])
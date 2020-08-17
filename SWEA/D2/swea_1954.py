import sys

sys.stdin = open("./input_data/input_1954.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    print(arr)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    d = 0

    wall == False

    def Wall():
        

    for i in range(1, N ** 2 + 1):
        arr[0+dy[d]][0+dx[d]] = i
        if wall == True:
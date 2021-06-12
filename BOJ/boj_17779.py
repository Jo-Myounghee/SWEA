def main():
    global answer

    def check(x, y):
        temp = 1e9
        for d2 in range(1, N-y):
            for d1 in range(1, N-x-d2):
                temp = min(temp, sum_people(x, y, d1, d2))
        return temp

    def sum_people(x, y, d1, d2):
        border = [[False] * N for _ in range(N)]
        for i in range(d1):
            border[y-i][x+i] = True
            border[y-d1+d2+i][x+d1+d2-i] = True
        for i in range(d2):
            border[y-d1+i][x+d1+i] = True
            border[y+d2-i][x+d2-i] = True
        nums = [0] * 5
        # 1
        for _y in range(y):
            for _x in range(x+d1+1):
                if border[_y][_x]:
                    break
                nums[0] += board[_y][_x]
        # 2
        for _y in range(y-d1+d2+1):
            for _x in range(N-1, x+d1, -1):
                if border[_y][_x]:
                    break
                nums[1] += board[_y][_x]
        # 3
        for _y in range(y, N):
            for _x in range(x+d2):
                if border[_y][_x]:
                    break
                nums[2] += board[_y][_x]
        # 4
        for _y in range(y-d1+d2+1, N):
            for _x in range(N-1, x+d2-1, -1):
                if border[_y][_x]:
                    break
                nums[3] += board[_y][_x]
        # 5
        nums[4] = (SUM - sum(nums))
        return max(nums)-min(nums)

    for y in range(N-1):
        for x in range(N-1):
            answer = min(answer, check(x, y))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
SUM = 0
for i in range(N):
    SUM += sum(board[i])
answer = 1e9
main()
print(answer)
def main():
    board = [list(map(int, input().split())) for _ in range(9)]

    def row():
        for i in range(9):
            if sum(board[i]) != 45:
                return False
        return True

    def col():
        for x in range(9):
            _sum = 0
            for y in range(9):
                _sum += board[y][x]
            if _sum != 45:
                return False
        return True

    def block():
        for i in range(1, 4):
            for j in range(1, 4):
                _sum = 0
                for y in range(3*(i-1), 3*i):
                    for x in range(3*(j-1), 3*j):
                        _sum += board[y][x]
                if _sum != 45:
                    return False
        return True

    if row() * col() * block():
        return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    print('#{} {}'.format(tc, main()))
'''
1
4
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
'''
def main(tc):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = -1

    def get_cycle(x, y, d1, d2):
        visited = [False] * 101
        cnt = 0
        for i in range(d1):
            d = board[y-i][x+i]
            if y-i < 0:
                return -1
            if visited[d]:
                return -1
            visited[d] = True
            d = board[y-d1+d2+i][x+d1+d2-i]
            if y-d1+d2+i < 0 or x+d1+d2-i < 0:
                return -1
            if visited[d]:
                return -1
            visited[d] = True
            cnt += 2
        for j in range(d2):
            d = board[y-d1+j][x+d1+j]
            if y-d1+j < 0:
                return -1
            if visited[d]:
                return -1
            visited[d] = True
            d = board[y+d2-j][x+d2-j]
            if y+d2-j < 0 or x+d2-j < 0:
                return -1
            if visited[d]:
                return -1
            visited[d] = True
            cnt += 2
        return cnt

    def start(x, y):
        answer = -1
        for d2 in range(1, N-y):
            for d1 in range(1, N-d2-x):
                answer = max(answer, get_cycle(x, y, d1, d2))
        return answer

    for y in range(1, N-1):
        for x in range(N-2):
            answer = max(answer, start(x, y))
    print('#{} {}'.format(tc, answer))


T = int(input())
for tc in range(1, T+1):
    main(tc)
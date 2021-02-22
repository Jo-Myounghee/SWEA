# N이 짝수이면 -> 다 0
# N이 홀수이면 -> 폭탄인지 아닌지 확인한다 ->
    # N //= 2 -> N번만큼 반복
    # 시간은 하나씩 증가
    # 지금 상태가 땅이라면 -> 그 다음 상태는 폭탄
    # 지금 폭탄 -> 다음 상태에서 인접한 땅이 터져야함

    # 지금->다음 : 슬라이딩 윈도우 기법을 사용하세욧
    #

def bomb(n):
    global R, C
    if n == 0:
        temp = board
    else:
        temp = answer[n-1]
    for y in range(R):
        for x in range(C):
            if temp[y][x] == 'O':
                answer[n][y][x] = '.'
                for i in range(4):
                    tx = x + dir[i][0]
                    ty = y + dir[i][1]
                    if 0 <= tx < C and 0 <= ty < R and answer[n][ty][tx] == 'O':
                        answer[n][ty][tx] = '.'


R, C, N = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

answer = [[['O']*C for _ in range(R)] for _ in range(2)]

# N이 짝수이면
if N % 2 == 0:
    for _ in range(R):
        print('O'*C)

# N이 1이면
elif N==1:
    for i in range(R):
        print(*board[i], sep="")

# N이 홀수이면 (1초 지난 후 / 3초 지난 후)
else:
    bomb(0)
    # 3초 지난 후
    if N % 4 == 3:
        for i in range(R):
            print(*answer[0][i], sep="")
    # 1초 지난 후
    else:
        bomb(1)

        for i in range(R):
            print(*answer[1][i], sep="")


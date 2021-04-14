from collections import deque

def get(x, y):
    # 방향에 따라 한 줄씩 queue에 숫자 담기 (0 제외)
    if board[y][x]:
        q.append(board[y][x])
        board[y][x] = 0

def merge(x, y, dx, dy):
    # 한 줄당 queue
    while q:
        # queue에서 하나씩 뽑아서
        num = q.popleft()
        # 만약 현재 위치에 처음 온거라면
        if not board[y][x]:
            # 숫자 담아주기
            board[y][x] = num
        # 만약 현재 위치에 있는 숫자와 지금 뽑은 숫자가 같다면,
        elif board[y][x] == num:
            # 숫자 2배하고
            board[y][x] = num*2
            # 자리 이동
            x, y = x+dx, y+dy
        # 현재 위치에 있는 숫자와 지금 뽑은 숫자가 같지 않다면,
        else:
            # 위치 이동
            x, y = x+dx, y+dy
            # 후에 숫자 담기
            board[y][x] = num

def move(k):
    global N
    # 왼쪽으로 밀었을 때
    if k == 0:
        for y in range(N):
            for x in range(N):
                get(x, y)
            merge(0, y, 1, 0)
    # 오른쪽으로 밀었을 때
    elif k == 1:
        for y in range(N):
            for x in range(N-1, -1, -1):
                get(x, y)
            merge(N-1, y, -1, 0)
    # 위로 밀었을 때
    elif k == 2:
        for x in range(N):
            for y in range(N):
                get(x, y)
            merge(x, 0, 0, 1)
    # 아래로 밀었을 때
    else:
        for x in range(N):
            for y in range(N-1, -1, -1):
                get(x, y)
            merge(x, N-1, 0, -1)

def solve(cnt):
    global board, ans, N
    # 5번째 이동이라면
    if cnt == 5:
        # 기존의 최댓 값과 현재 board의 최댓 값 중 더 큰 것으로 갱신
        for i in range(N):
            ans = max(ans, max(board[i]))
        return
    # board 복제
    temp = [x[:] for x in board]
    # k는 상, 하, 좌, 우
    for k in range(4):
        move(k)
        solve(cnt+1)
        # board 초기화(방향을 바꿀 때마다 원래의 보드를 사용해야함)
        board = [x[:] for x in temp]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
q = deque()

solve(0)
print(ans)
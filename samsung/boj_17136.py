def isok(_x, _y, size):
    for y in range(_y, _y + size):
        for x in range(_x, _x + size):
            if x < 0 or x >= 10 or y < 0 or y >= 10 or board[y][x] == 0:
                return False
    return True

def attach(_x, _y, size, tf):
    for y in range(_y, _y + size):
        for x in range(_x, _x + size):
            board[y][x] = tf

def dfs(_x, _y, cnt):
    global minAns

    # 완탐시 줄바꿈이 필요할 때
    if _x >= 10:
        _x -= 10
        _y += 1

    # 마지막 지점에 도착했을 때
    if (_x, _y) == (9, 9):
        minAns = min(cnt, minAns)
        return

    # 만약 count가 minAns보다 클 때
    if cnt >= minAns:
        return

    maxSize = 0

    # 붙일 수 있는 가장 큰 색종이의 크기
    for size in range(5, 0, -1):
        if isok(_x, _y, size):
            maxSize = size
            break
    # 탐색하다가 색종이를 붙일 수 있는 지점을 만나면
    if board[_y][_x] == 1:
        # 가장 큰 사이즈의 색종이부터 붙여본다.
        for size in range(maxSize, 0, -1):
            # 현재 사용하려는 색종이의 사용 횟수가 5번을 넘지 않는다면
            if papers[size] > 0:
                # 색종이를 붙인다.
                attach(_x, _y, size, 0)
                # 색종이 사용 횟수 갱신
                papers[size] -= 1
                # 완탐 고고
                dfs(_x, _y, cnt+1)
                # 색종이를 뗀다
                attach(_x, _y, size, 1)
                # 색종이 사용 횟수 갱신
                papers[size] += 1

    # 색종이를 붙일 수 없는 지점이면 계속 탐색 고고
    else:
        dfs(_x+1, _y, cnt)

minAns = 1e9
papers = [-1, 5, 5, 5, 5, 5]
board = [list(map(int, input().split())) for _ in range(10)]
dfs(0, 0, 0)
print(minAns if minAns < 1e9 else -1)
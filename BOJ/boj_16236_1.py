from collections import deque

def bfs(x, y):
    global N
    dir = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    q = deque()
    q.append((x, y, 0))

    eatq = deque()

    eat_time = 0
    eat_num = 0

    level = 2

    min_x = x
    min_y = y

    while True:
        eat = False
        visited = [[False] * N for _ in range(N)]
        visited[min_y][min_x] = True
        while q:
            # q 에서 빼요
            now_x, now_y, cnt = q.popleft()
            print(now_x+1, now_y+1, '좌표')
            # 처음에는 상어위치 1개니까 q에 하나밖에없다는거 -> 첫상어의 위치
            # 두번째 상어의 위치 두번째 턴
            if board[now_y][now_x] == 9:
                board[now_y][now_x] = 0

            # 물고기야?
            if board[now_y][now_x] != 0 and board[now_y][now_x] < level:
            # end flag! 먹을 수 있는 물고기가 1마리라도 있다는 뜻
                eat = True
            # 물고기면 일단 eatq에 추가
                eatq.append((now_x, now_y, cnt))
                while q:
                        # 안에있는 좌표중에 물고기가 있는지 없는지를 확인해요
                    test_x, test_y, cnt = q.popleft()
                    if board[test_y][test_x] != 0 and board[test_y][test_x] < level:
                        # 좌표가 물고기라면 eatq에 추가
                        eatq.append((test_x, test_y, cnt))
            # 이곳에서 q는 다 비워졋어!
            # 물고기가 아니야?

            # 아니라면 갈 수 있는 위치라면
            else:
            # 4방탐색
                for i in range(4):
                    test_x = now_x + dir[i][0]
                    test_y = now_y + dir[i][1]
                # visited으로 중복처리를 할꺼잖아
                    if 0 <= test_x < N and 0 <= test_y < N and visited[test_y][test_x] == False and board[test_y][test_x] <= level:
                        visited[test_y][test_x] = True
                        q.append((test_x, test_y, cnt+1))
                # 처음에 시작할 때

        if not eat:
            break

        #드디어 물고기를 먹자고
        min_x = -1
        min_y = -1
        min_cnt = 1e9
        #         #eatq에 있잖아

        while eatq:
        # eatq를 빼면서 확인해
            eat_x, eat_y, eat_cnt = eatq.popleft()
        # 거리는 항상 같을 수 밖에 없어 동일
            if eat_cnt < min_cnt:
                min_cnt = eat_cnt
                min_x = eat_x
                min_y = eat_y
        # 행인지?
        # eatx, eaty 먹을 좌표 좌표 업데이트
        # 행이 같다면?
            elif eat_cnt == min_cnt:
                if eat_y < min_y:
                    min_cnt = eat_cnt
                    min_x = eat_x
                    min_y = eat_y
        # 열인지?
        # eatx, eaty 먹을 좌표 좌표 업데이트
                elif eat_y == min_y:
                    if eat_x < min_x:
                        min_cnt = eat_cnt
                        min_x = eat_x
                        min_y = eat_y

        #eatq를 빠져나오면?
        if min_x != -1:
        #최종적인 eatx, eaty
            print(board[min_y][min_x], '값')
            board[min_y][min_x] = 0
        #최종적인 좌표인 이놈의 물고기를 먹고 얘의 거리를 ans더해가
            eat_time += min_cnt
            print(eat_time, 'eat_time', min_y, min_x, '(y, x)', '좌표', level, '레벨')
        # 먹을 때마다 eat_num 추가해주기, 레벨 업
            eat_num += 1
            if eat_num == level:
                eat_num = 0
                level += 1
        #그리고 나서 최종 좌표인 eatx, eaty -> q에 담아요
            q.append((min_x, min_y, 0))

    return eat_time

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for y in range(N):
    for x in range(N):
        if board[y][x] == 9:
            start_x, start_y = x, y

tmp_ans = bfs(start_x, start_y)
print(tmp_ans)

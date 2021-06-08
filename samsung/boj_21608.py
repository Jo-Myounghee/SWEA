from collections import deque

def is_board(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def seat():
    global order, room

    def empty_seat(st):
        seat_info = [] # (like_cnt, 위치x, 위치y)
        for y in range(N):
            for x in range(N):
                if room[y][x] == 0:
                    # 주변을 둘러보자
                    like_cnt = 0
                    empty_cnt = 0
                    for i in range(4):
                        tx, ty = x + dx[i], y + dy[i]
                        if is_board(tx, ty):
                            if room[ty][tx] in like_info[st]:
                                like_cnt += 1
                            elif room[ty][tx] == 0:
                                empty_cnt += 1
                    seat_info.append((like_cnt, empty_cnt, x, y))
                else:
                    continue
        seat_info.sort(key=lambda x: (-x[0], -x[1], x[3], x[2]))
        seat_pos = (seat_info[0][2], seat_info[0][3]) # x, y값
        return seat_pos

    for i in range(N*N):
        now_student = order.popleft()
        # 앉을 자리를 구해보자
        _x, _y = empty_seat(now_student)
        room[_y][_x] = now_student


def cal_like():
    like_score = [0, 1, 10, 100, 1000]
    total_score = 0

    for y in range(N):
        for x in range(N):
            now_st = room[y][x]
            like_cnt = 0
            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]
                if is_board(tx, ty) and room[ty][tx] in like_info[now_st]:
                    like_cnt += 1
            total_score += like_score[like_cnt]
    return total_score


N = int(input())
like_info = dict() # 좋아하는 친구 정보
room = [[0]*N for _ in range(N)] # 교실
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
order = deque()
for _ in range(N*N):
    inputs = list(map(int, input().split()))
    like_info[inputs[0]] = inputs[1:]
    order.append(inputs[0])
seat()
print(cal_like())
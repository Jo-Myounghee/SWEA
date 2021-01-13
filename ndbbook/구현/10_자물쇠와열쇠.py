# 90도 시계 방향 회전
def rot(key):
    N = len(key)
    new_key = [[0] * N for i in range(N)]
    for y in range(N):
        for x in range(N):
            new_key[y][x] = key[N - x - 1][y]
    return new_key


def solution(key, lock):
    N = len(key)
    M = len(lock)
    key_len = 0
    lock_len = 0
    for y in range(N):
        for x in range(N):
            if key[y][x] == 1:
                key_len += 1
    for y in range(M):
        for x in range(M):
            if lock[y][x] == 0:
                lock_len += 1

    if key_len < lock_len:
        # print('열쇠구멍이 너무 커')
        return False

    if M == N and lock_len == key_len:
        # print('같을 때')
        # 회전만 하기
        for i in range(4):
            key = rot(key)
            cnt = 0
            for y in range(M):
                for x in range(M):
                    if key[y][x] != lock[y][x]:
                        cnt += 1
                    else:
                        cnt = 0
            if cnt == (M * M):
                return True
        return False

    else:
        big_lock = [[2] * (M + N + 1) for i in range(M + N + 1)]
        for y in range(N - 1, N - 1 + M):
            for x in range(N - 1, N - 1 + M):
                big_lock[y][x] = lock[(y - N + 1)][(x - N + 1)]
        # for i in range(len(big_lock)):
        #     print(big_lock[i])

    # 회전
    for i in range(4):
        # print('다름')
        key = rot(key)
        # 이동
        for k in range(len(big_lock) - N):
            for t in range(len(big_lock) - N):
                open_key = 0
                cnt = 0
                for y in range(N):
                    for x in range(N):
                        if key[y][x] != big_lock[y + k][x + t]:
                            cnt += 1
                            if key[y][x] == 1 and big_lock[y + k][x + t] == 0:
                                open_key += 1
                        elif key[y][x] == 1 and big_lock[y + k][x + t] == 1:
                            cnt = 0
                        else:
                            cnt += 1
                # print(cnt, 'cnt')
                # print(open_key, 'open_key')
                if cnt == (N * N) and open_key == lock_len:
                    return True
    return False
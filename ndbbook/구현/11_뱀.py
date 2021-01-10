# https://www.acmicpc.net/problem/3190
import sys
sys.stdin = open('11input.txt', 'r')
# sys.stdin = open('11input1.txt', 'r')
# sys.stdin = open('11input2.txt', 'r')

# 이 곳은 길인가
def isWall(x, y):
    global now_snake
    if x <= 0 or x > N or y <= 0 or y > N:
        print('벽에 부딪혔다.')
        return False
    elif [x, y] in now_snake: # 자기 몸인 경우
        print('뱀에 부딪혔다')
        return False
    return True

N = int(sys.stdin.readline())

# 사과 위치 : 현재 (y, x)로 되어있음.
apple_lst = [list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))]

# 뱀의 방향 변환 갯수
snake_dir = [list(sys.stdin.readline().split()) for i in range(int(sys.stdin.readline()))]

# 판
board = [[0] * (N+1) for _ in range(N+1)]
# 방향 (idx+1인경우 오른쪽으로 90도 회전, idx-1인 경우 왼쪽으로 90도 회전)
dir_lst = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 현재 머리가 향하고 있는 방향의 idx
now_dir = 0
# 현재 뱀 꼬리부터 머리까지의 위치 (x, y), pop, append를 사용할 예정
now_snake = [[1, 1]]
# 현재 시간
cnt = 0

while True:
    if len(snake_dir) and int(snake_dir[0][0]) == cnt:
        change_dir = snake_dir.pop(0)
        # snake_dir[0][1]에 따라 dir 바꾸기 (만약 'L'이라면 -1 'D'라면 +1)
        if change_dir[1] == 'L':
            now_dir = (now_dir + 3) % 4
        else:
            now_dir = (now_dir + 1) % 4
    test_x = now_snake[-1][0] + dir_lst[now_dir][0]
    test_y = now_snake[-1][1] + dir_lst[now_dir][1]
    if isWall(test_x, test_y):
        if not [test_y, test_x] in apple_lst:
            now_snake.pop(0)
        else:
            apple_lst.remove([test_y, test_x])
        now_snake.append([test_x, test_y])
        cnt += 1
    else:
        print(cnt+1)
        break



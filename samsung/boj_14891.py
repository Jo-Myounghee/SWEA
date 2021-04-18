from collections import deque

def score():
    ans = 0
    for i in range(4):
        if status[i][0] == 1:
            ans += (2 ** i)
    return ans

def rotate(i, d):
    global status
    # 반시계 방향
    if d == -1:
        a = status[i].popleft()
        status[i].append(a)
    # 시계 방향
    elif d == 1:
        a = status[i].pop()
        status[i].appendleft(a)

def solve(i, d):
    temp_dir = [[1, -1, 1, -1], [-1, 1, -1, 1]]
    dir = temp_dir[0] if temp_dir[0][i] == d else temp_dir[1]
    for i in range(4):
        if connection[i]:
            rotate(i, dir[i])

def isConnection(i):
    global connection, visited
    if not visited[i]:
        visited[i] = True
        if i-1 >= 0:
            if status[i][6] + status[i-1][2] == 1:
                connection[i-1] = True
                isConnection(i-1)
        if i+1 < 4:
            if status[i][2] + status[i+1][6] == 1:
                connection[i+1] = True
                isConnection(i+1)
    return

# 12시방향부터 시계방향 순서대로, N극은 0, S극은 1
status = [deque(list(map(int, input()))) for _ in range(4)]
K = int(input())
# (회전시킨 톱니바퀴의 번호, 1인경우 시계방향/-1인경우 반시계방향)
orders = [tuple(map(int, input().split())) for _ in range(K)]
for order in orders:
    idx, dir = order[0]-1, order[1]
    connection = [False]*4
    visited = [False] * 4
    connection[idx] = True
    isConnection(idx)
    solve(idx, dir)

print(score())


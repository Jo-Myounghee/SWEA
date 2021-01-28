'''
1
8
0 0
7 0

-> 5
'''
# BFS
def BFS(x, y):
    dir = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
    global I, end_x, end_y
    q = [[x, y, 0]]
    while q:
        nx, ny, cnt = q.pop(0)
        if nx == end_x and ny == end_y:
            return cnt
        for i in range(8):
            tx = nx + dir[i][0]
            ty = ny + dir[i][1]
            if 0 <= tx < I and 0 <= ty < I and visited[ty][tx] == 0:
                visited[ty][tx] = 1
                q.append([tx, ty, cnt+1])


T = int(input())
for _ in range(T):
    I = int(input())
    now_x, now_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[0] * I for _ in range(I)]
    print(BFS(now_x, now_y))

    

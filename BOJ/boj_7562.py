'''
1
8
0 0
7 0

-> 5
'''
# BFS
def move(x, y):
    dir = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
    for i in range(8):


T = int(input())
for _ in range(T):
    I = int(input())
    now_x, now_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    

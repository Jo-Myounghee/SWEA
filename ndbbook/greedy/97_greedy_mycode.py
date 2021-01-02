'''
3 3
3 1 2
4 1 4
2 2 2
'''
'''
2 4
7 3 1 8
3 3 3 4
'''
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

max_num = 0
for i in range(N):
    if min(lst[i]) > max_num:
        max_num = min(lst[i])
print(max_num)
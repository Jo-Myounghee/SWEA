'''
6 60
5
1 2 30
2 5 70
5 6 60
3 4 40
1 6 40

4 40
3
1 4 40
2 3 40
3 4 40
'''
N, C = map(int, input().split())
M = int(input())
items = [[] for _ in range(N)]
inputs = [list(map(int, input().split())) for _ in range(M)]
inputs.sort()
for i in range(M):
    s, g, item = inputs[i]
    items[s].append([g, item])

sends = [0] * (N+1)

now_items = 0

for i in range(1, N):
    item = items[i]
    now_items -= sends[i]
    for j in range(len(item)):
        item_idx = item[j][0]
        if now_items + item[j][1] <= C:
            item_val = item[j][1]
        else:
            item_val = (C-now_items)
        
        now_items += item_val
        sends[item_idx] += item_val

print(sum(sends))
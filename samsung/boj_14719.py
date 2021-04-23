H, W = map(int, input().split())
lst = list(map(int, input().split()))
max_height = max(lst)
max_idx = lst.index(max_height)
answer = 0
temp_max = 0
for i in range(0, max_idx):
    temp_max = max(temp_max, lst[i])
    answer += temp_max-lst[i]
temp_max = 0
for i in range(W-1, max_idx, -1):
    temp_max = max(temp_max, lst[i])
    answer += temp_max-lst[i]
print(answer)

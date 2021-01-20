N = int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]
inputs.sort()
heights = [0] * (inputs[-1][0]+1)

max_val = 0
max_idx = 0
for i in range(N):
    if max_val < inputs[i][1]:
        max_val = inputs[i][1]
        max_idx = inputs[i][0]
    heights[inputs[i][0]] = inputs[i][1]

sum = max_val
j = inputs[0][0]
prev_height = inputs[0][1]
while j < max_idx:
    if heights[j] and prev_height < heights[j]:
        prev_height = heights[j]
    sum += prev_height
    j += 1

k = inputs[-1][0]
prev_height = inputs[-1][1]
while k > max_idx:
    if heights[k] and prev_height < heights[k]:
        prev_height = heights[k]
    sum += prev_height
    k -= 1

print(sum)
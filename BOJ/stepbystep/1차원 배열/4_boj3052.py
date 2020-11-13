lst = [0] * 42
cnt = 0
for i in range(10):
    lst[int(input()) % 42] += 1
for i in range(42):
    if lst[i]:
        cnt += 1
print(cnt)
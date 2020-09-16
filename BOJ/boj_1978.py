# import math
input()
num_lst = list(map(int, input().split()))
cnt = 0
for num in num_lst:
    flag = True
    if num <= 1:
        continue
    for i in range(2, (num//2)+1):
        if num % i == 0:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)


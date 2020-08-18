import sys

sys.stdin = open("./input_data/input_1926.txt", "r")

N = int(input())
lst = [3, 6, 9]
for i in range(1, N+1):
    k = str(i)
    cnt = 0
    for j in lst:
        j = str(j)
        for t in range(len(k)):
            if j in k[t]:
                cnt += 1
    if cnt == 0:
        result = i
    else:
        result = '-' * cnt
    print(result, end=' ')

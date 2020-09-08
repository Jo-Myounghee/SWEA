from sys import stdin

T = int(stdin.readline().rstrip('\n'))
arr = [[0] * 100 for _ in range(100)]
for tc in range(T):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[b+i][a+j] = 1

cnt = 0
for i in range(100):
    cnt += arr[i].count(1)

print(cnt)
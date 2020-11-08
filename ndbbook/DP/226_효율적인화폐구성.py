'''
inputs 1
2 15
2
3

inputs 2
3 4
3
5
7

output 1
5

output 2
-1
'''

N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
d = [10001] * (M+1)

d[0] = 0
for i in range(N):
    for j in range(coins[i], M+1):
        d[j] = min(d[j], d[j-coins[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
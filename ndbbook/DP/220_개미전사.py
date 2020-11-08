'''
inputs
4
1 3 1 5
output
8
'''

N = int(input())
eats = list(map(int, input().split()))
d = [0] * 100

d[0] = eats[0]
d[1] = max(eats[0], eats[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+eats[i])

print(d[N-1])
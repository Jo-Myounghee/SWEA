N = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0

for i in range(N):
    a[i] -= b
    cnt += 1
    if a[i] > 0:
        cnt += (a[i]//c)
        if a[i] % c != 0:
            cnt += 1

print(cnt)
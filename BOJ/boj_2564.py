def dist(d, o):
    if d == 1:
        return TOT - o
    elif d == 2:
        return Y + o
    elif d == 3:
        return o
    else:
        return TOT - (X + o)

X, Y = map(int, input().split())
TOT = (X + Y) * 2
N = int(input())
shop = []
for i in range(N + 1):
    D, O = map(int, input().split())
    wd = dist(D, O)
    if i == N:
        sp = wd
    else:
        shop.append(wd)
SUM = 0
for i in range(N):
    wat = abs(sp - shop[i])
    rwat = TOT - wat
    SUM += min(wat, rwat)
print(SUM)

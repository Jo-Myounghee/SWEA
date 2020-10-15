X, Y = map(int, input().split())
N = int(input())
xlst = []
ylst = []
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        xlst.append(y)
    elif x == 1:
        ylst.append(y)

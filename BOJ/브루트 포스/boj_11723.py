import sys

N = int(sys.stdin.readline())
S = [False] * 21
for i in range(N):
    order = sys.stdin.readline().strip().split()
    if len(order) == 1:
        if order[0] == 'all':
            S = [False] + [True]*20
        else:
            S = [False] * 21
    else:
        order, x = order[0], int(order[1])
        if order == 'add':
            S[x] = True
        elif order == 'remove':
            S[x] = False
        elif order == 'check':
            if S[x]:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if S[x]:
                S[x] = False
            else:
                S[x] = True

# print(*answer, sep="\n")
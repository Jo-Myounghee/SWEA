import sys
N = int(input())
dices = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum = []
couple = {0: 5, 1: 3, 2: 4, 5: 0, 3: 1, 4: 2}

def maxnum(lst):
    if lst[0] != 6 and lst[1] != 6:
        return 6
    elif lst[0] != 5 and lst[1] != 5:
        return 5
    else:
        return 4

for i in range(6):
    SUM = 0
    idx = i
    updown = [dices[0][i], dices[0][couple[i]]]
    SUM += maxnum(updown)
    idx = couple[idx]
    for j in range(1, N):
        idx = dices[j].index(dices[j - 1][idx])
        updown = [dices[j][idx], dices[j][couple[idx]]]
        SUM += maxnum(updown)
        idx = couple[idx]

    sum.append(SUM)
print(max(sum))
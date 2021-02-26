N = int(input())

gools = []

for i in range(N):
    lst = list(map(str, input().split()))
    n = lst.pop(0)
    gools.append(lst)

gools.sort()

result = [[] for _ in range(len(gools))]

for i in range(len(gools)):
    idx = 0

    if i > 0:
        cnt = 0
        for k in range(min(len(gools[i]), len(gools[i-1]))):
            if gools[i][k] != gools[i-1][k]:
                idx = k
                break
            else:
                cnt += 1

        if cnt == min(len(gools[i]), len(gools[i-1])):
            idx = cnt

        if idx == 0:
            for j in range(len(gools[i])):
                result[i].append('--' * j + gools[i][j])

        else:
            for j in range(idx, len(gools[i])):
                result[i].append('--' * j + gools[i][j])

    else:
        for j in range(idx, len(gools[i])):
            result[i].append('--' * j + gools[i][j])

for i in range(len(result)):
    print(*result[i], sep="\n")
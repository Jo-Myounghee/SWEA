def DFS(x, y, total, cnt):
    global minAns

    if total > minAns:
        return

    if cnt == N:
        total += (abs(x-hx)+abs(y-hy))
        if total < minAns:
            minAns = total
        return

    for i in range(N):
        x1, y1 = homes[i]
        if not visited[i]:
            visited[i] = True
            temp = (abs(x-x1) + abs(y-y1))
            DFS(x1, y1, total+temp, cnt+1)
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    bx, by = data[0:2]
    hx, hy = data[2:4]

    homes = []
    for i in range(2, N+2):
        homes.append(data[i*2:i*2+2])

    visited = [False]*N
    minAns = 1e9
    DFS(bx, by, 0, 0)
    print('#{} {}'.format(tc, minAns))
def DP(n, p):
    global N, maxAns

    if n == N:
        return
    tn, pn = lists[n]
    np = p + pn
    if n+tn <= N and money[n+tn] < np:
        money[n+tn] = np
        DP(n+tn, np)
        for i in range(n+tn, N):
            DP(i, np)
    elif n+tn == N and money[n+tn] < np:
        money[n+tn] = np

N = int(input())
lists = [list(map(int, input().split())) for _ in range(N)]
money = [0] * (N+1)
for i in range(N):
    DP(i, 0)
print(max(money))

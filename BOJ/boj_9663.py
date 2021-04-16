# 백트래킹

def adj(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True

def dfs(n):
    global ans, N
    if n == N:
        ans += 1
    else:
        for i in range(N):
            row[n] = i
            if adj(n):
                dfs(n+1)

N = int(input())
row=[0]*N
ans = 0
dfs(0)
print(ans)

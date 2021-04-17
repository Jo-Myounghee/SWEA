def solve(cnt, idx):
    global ans
    if idx == N:
        return
    if cnt == N//2:
        s1, s2 = 0, 0
        for i in range(N):
            for j in range(N):
                if team[i] and team[j]:
                    s1 += scores[i][j]
                if not team[i] and not team[j]:
                    s2 += scores[i][j]
        ans = min(ans, abs(s1-s2))
        return
    team[idx] = True
    solve(cnt+1, idx+1)
    team[idx] = False
    solve(cnt, idx+1)

N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
team = [False]*N
ans = 1e9

solve(0, 0)
print(ans)
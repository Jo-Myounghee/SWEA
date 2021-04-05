N, K = map(int, input().split())
inputs = [[0]*2] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]
print(inputs)
for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= inputs[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-inputs[i][0]] + inputs[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])


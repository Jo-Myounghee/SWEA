N, K = map(int, input().split())
inputs = list(map(int, input().split()))
inputs.sort()

for i in range(K):
    L, R, X = map(int, input().split())
    for j in range(L-1, R):
        inputs[j] += X
    inputs.sort()

print(*inputs)
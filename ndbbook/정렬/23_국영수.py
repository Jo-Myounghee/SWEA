N = int(input())

inputs = [list(map(str, input().split())) for _ in range(N)]

inputs.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(inputs[i][0])
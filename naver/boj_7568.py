N = int(input())
person = [1]*N
inputs = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if i == j:
            continue
        else:
            if inputs[i][0] > inputs[j][0] and inputs[i][1] > inputs[j][1]:
                person[j] += 1
            elif inputs[i][0] < inputs[j][0] and inputs[i][1] < inputs[j][1]:
                person[i] += 1

print(*person)

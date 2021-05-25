def perm(k, temp):
    global N, inputs, answer, max_val

    if k == N:
        if temp > max_val:
            max_val = temp
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            diff = abs(answer[-1]-inputs[i])
            temp += diff
            answer.append(inputs[i])
            perm(k+1, temp)
            visited[i] = False
            temp -= diff
            answer.pop()

N = int(input())
inputs = list(map(int, input().split()))
max_val = 0

for i in range(N):
    visited = [False]*N
    answer = [inputs[i]]
    visited[i] = True
    perm(1, 0)

print(max_val)
def func(cnt):
    global N, M, answer
    if cnt == M:
        print(*answer)
        return
    
    for i in range(N):
        answer.append(inputs[i])
        func(cnt+1)
        answer.pop()

N, M = map(int, input().split())
inputs = list(map(int, input().split()))
inputs.sort()
answer = []
func(0)

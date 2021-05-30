def func(s, cnt):
    global N, M, answer
    if cnt == M:
        print(*answer)
        return
    for i in range(s, N):
        if len(answer) > 0 and answer[-1] > inputs[i]:
            continue
        if not visited[i]:
            answer.append(inputs[i])
            visited[i] = True
            func(s+1, cnt+1)
            visited[i] = False
            answer.pop()

N, M = map(int, input().split())
inputs = list(map(int, input().split()))
inputs.sort()
answer = []
visited = [False]*N
func(0, 0)
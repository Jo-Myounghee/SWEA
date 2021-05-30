def func(s, cnt):
    global N, M, answer, visited
    if cnt == M:
        print(*answer)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            answer.append(inputs[i])
            func(s+1, cnt+1)
            visited[i] = False
            answer.pop()

N, M = map(int, input().split())
inputs = list(map(int, input().split()))
inputs.sort()
answer = []
visited = [False]*N
func(0, 0)
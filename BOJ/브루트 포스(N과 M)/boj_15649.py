def func(cnt):
    global N, M, answer, visited
    if cnt == M:
        print(*answer)
        return
    for i in range(1, N+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            func(cnt+1)
            visited[i] = False
            answer.pop()

N, M = map(int, input().split())
answer = []
visited = [False] * (N+1)
func(0)
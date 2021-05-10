def perm(n):
    global answer, visited
    if n == N:
        print(*answer, sep=" ")
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            answer.append(lst[i])
            perm(n+1)
            visited[i] = False
            answer.pop()

N = int(input())
lst = list(range(1, N+1))
visited = [False] * N
answer = []
perm(0)

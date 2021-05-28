def func(cnt):
    global N, M, answer
    if cnt == M:
        print(*answer)
        return
    for i in range(1, N+1):
        answer.append(i)
        func(cnt+1)
        answer.pop()

N, M = map(int, input().split())
answer = []
func(0)
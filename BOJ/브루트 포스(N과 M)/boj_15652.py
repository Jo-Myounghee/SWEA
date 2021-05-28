def func(s, cnt):
    global N, M, answer
    if cnt == M:
        print(*answer)
        return
    for i in range(s, N+1):
        if len(answer)>0 and answer[-1] > i:
            continue
        answer.append(i)
        func(s, cnt+1)
        answer.pop()

N, M = map(int, input().split())
answer = []
func(1, 0)
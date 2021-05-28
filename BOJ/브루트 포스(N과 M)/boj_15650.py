def func(s, cnt):
    global N, M, answer
    if cnt == M:
        print(*answer)
        return
    
    for i in range(s, N+1):
        answer.append(i)
        func(i+1, cnt+1)
        answer.pop()

N, M = map(int, input().split())
answer = []
func(1, 0)
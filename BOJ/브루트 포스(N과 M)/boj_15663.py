def func(cnt):
    global N, M, answer, answer_lst
    if cnt == M:
        now = " ".join(map(str, answer))
        if not now in answer_lst:
            answer_lst[now] = True
            real_answer.append(now)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            answer.append(inputs[i])
            func(cnt+1)
            answer.pop()
            visited[i] = False


N, M = map(int, input().split())
inputs = list(map(int, input().split()))
inputs.sort()
answer = []
answer_lst = dict()
real_answer = []
visited = [False] * N
func(0)
print(*real_answer, sep="\n")


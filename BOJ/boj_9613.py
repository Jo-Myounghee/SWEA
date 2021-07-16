def GCD(lst):
    a, b = lst
    while b:
        a, b = b, a % b
    return a

def comb(cnt, N, start):
    global answer, sum_answer
    if cnt == N:
        sum_answer += GCD(answer)
        return
    else:
        for i in range(start, len(lst)):
            answer.append(lst[i])
            comb(cnt+1, N, i+1)
            answer.pop()

N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    lst.pop(0)
    answer = []
    sum_answer = 0
    comb(0, 2, 0)
    print(sum_answer)

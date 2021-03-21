N = int(input())
answer = N
for i in range(N//5, -1, -1):
    if not (N - i*5)% 3:
        temp_ans = ((N-i*5)//3) + i
        if temp_ans < answer:
            answer = temp_ans
print(answer) if answer != N else print(-1)
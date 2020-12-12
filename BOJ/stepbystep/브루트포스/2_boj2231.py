N = int(input())
sol = 0
for i in range(N):
    answer = 0
    answer += i
    words = str(i)
    for j in range(len(words)):
        answer += int(words[j])
    if answer == N:
        sol = i
        break
print(sol)
N = int(input())
money = list(map(int, input().split()))
money.sort()
answer = 0
for i in range(N):
    answer += (money[i]*(N-i))
print(answer)
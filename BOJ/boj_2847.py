def cal():
    answer = 0
    for i in range(N - 1):
        if lst[i] >= lst[i + 1]:
            answer += (lst[i] - lst[i + 1] + 1)
            lst[i] -= (lst[i] - lst[i + 1] + 1)
    return answer

def isPlus():
    for i in range(N-1):
        if lst[i] >= lst[i+1]:
            return False
    return True

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0

while not isPlus():
    cnt += cal()

print(cnt)

# ------------------------------------

N = int(input())
lst = [int(input()) for _ in range(N)]
answer = 0
for i in range(N-1, 0, -1):
    if lst[i] <= lst[i-1]:
        num = lst[i-1] - lst[i] + 1
        lst[i-1] -= num
        answer += num
print(answer)

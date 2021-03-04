# 조합
def comb(k, idx):
    global inputs, answer, cnt

    if k == 2:
        # 여기서 바로 check
        if isSame(inputs[answer[0]], inputs[answer[1]]):
            cnt += 1
        return

    for i in range(len(inputs)):
        if i >= idx:
            if not visited[i]:
                visited[i] = True
                answer.append(i)
                comb(k+1, i+1)
                visited[i] = False
                answer.pop()

# 대소관계
def isSame(arr1, arr2):
    for i in range(len(arr1)-1):
        for j in range(i+1, len(arr1)):
            if arr1[i] < arr1[j] and arr2[i] >= arr2[j]:
                return False
            elif arr1[i] == arr1[j] and arr2[i] != arr2[j]:
                return False
            elif arr1[i] > arr1[j] and arr2[i] <= arr2[j]:
                return False
    return True
M, N = map(int, input().split())
inputs = []
for _ in range(M):
    inputs.append(list(map(int, input().split())))
answer = []
visited = [False] * len(inputs)
cnt = 0
comb(0, 0)

print(cnt)








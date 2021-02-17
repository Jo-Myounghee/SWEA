N = int(input())
inputs = list(map(int, input().split()))

if len(set(inputs)) == 1:
    print(0)

# 증가수열
prev = inputs[0]
change = -1
no_answer = False
for i in range(1, len(inputs)):
    if prev > inputs[i]:
        if change != -1:
            no_answer = True
            break
        change = i
        if i+1 < N and inputs[i+1]:

    prev = inputs[i]

# 감소수열
prev = inputs[0]
change = -1
no_answer = False
for i in range(1, len(inputs)):
    if prev < inputs[i]:
        if change != -1:
            no_answer = True
            break
        change = i

    prev = inputs[i]
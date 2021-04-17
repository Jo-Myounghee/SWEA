def cal(prev, n):
    global max_ans, min_ans, N
    if n == N:
        max_ans = max(max_ans, prev)
        min_ans = min(min_ans, prev)
        return
    # 덧셈
    if sign[0] > 0:
        add = prev + numbers[n]
        sign[0] -= 1
        cal(add, n+1)
        sign[0] += 1
    # 뺄셈
    if sign[1] > 0:
        sub = prev - numbers[n]
        sign[1] -= 1
        cal(sub, n+1)
        sign[1] += 1
    # 곱셈
    if sign[2] > 0:
        mul = prev * numbers[n]
        sign[2] -= 1
        cal(mul, n+1)
        sign[2] += 1
    # 나눗셈
    if sign[3] > 0:
        if prev >= 0:
            div = prev // numbers[n]
        else:
            div = -((-prev) // numbers[n])
        sign[3] -= 1
        cal(div, n+1)
        sign[3] += 1

N = int(input())
numbers = list(map(int, input().split()))
# 덧셈 뺄셈 곱셈 나눗셈
sign = list(map(int, input().split()))

max_ans = -1e9
min_ans = 1e9

cal(numbers[0], 1)

print(max_ans, min_ans, sep="\n")
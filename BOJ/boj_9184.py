def func(a, b, c):
    if a > 70 or b > 70 or c > 70:
        ans = func(70, 70, 70)
        for i in range(71, 101):
            for j in range(71, 101):
        return func(70, 70, 70)
    elif a < b < c:
        return func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
    else:
        return func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)

ans = -1
lst = [[[1] * 51 for _ in range(51)] for _ in range(51)] + [[[0] * 51 for _ in range(51)] for _ in range(51)] + [[[ans] * 51 for _ in range(51)] for _ in range(51)]
# print(lst)

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break 
    


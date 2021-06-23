def solution(n):
    lst = [[1, 0], [0, 1]]
    while True:
        if len(lst) > n:
            return f'{lst[n][0]} {lst[n][1]}'
        _0 = lst[-1][0] + lst[-2][0]
        _1 = lst[-1][1] + lst[-2][1]
        lst.append([_0, _1])


T = int(input())
for _ in range(T):
    print(solution(int(input())))
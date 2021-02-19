def powerset(s):
    x = len(s)
    for i in range(1 << x):
        print [s[j] for j in range(x) if (i & (1 << j))]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

(powerset(list(range(N))))

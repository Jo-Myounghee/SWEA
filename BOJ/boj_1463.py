'''
642 -> 10
643 -> 11

'''
def DP(n):
    lst[n] = lst[n-1] + 1
    if n % 3 == 0:
        lst[n] = min(lst[n], lst[n//3] + 1)
    if n % 2 == 0:
        lst[n] = min(lst[n], lst[n//2] + 1)
    return

N = int(input())

lst = [0]*(N+1)

for i in range(2, N+1):
    DP(i)

print(lst[N])
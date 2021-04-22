def solve():
    d[1], d[2] = p[1], p[1]+p[2]
    for i in range(3, n+1):
        d[i] = d[i-1]
        d[i] = max(d[i], d[i-2]+p[i])
        d[i] = max(d[i], d[i-3]+p[i-1]+p[i])

n = int(input())
d = [0]*(n+2)
p = [0]+[int(input()) for _ in range(n)]+[0]
solve()
print(d[n])
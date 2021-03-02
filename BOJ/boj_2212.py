N = int(input())
K = int(input())
lst = list(map(int, input().split()))
lst.sort()
dist = []
for i in range(1, len(lst)):
    dist.append(lst[i]-lst[i-1])
dist.sort()
print(sum(dist[:N-K]))

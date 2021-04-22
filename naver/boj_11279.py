import sys, heapq

N = int(input())
lst = []
for i in range(N):
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(lst, (-n, n))
    else:
        if lst:
            print(heapq.heappop(lst)[1])
        else:
            print(0)
import heapq, sys

arr = []
N = int(input())
i = 0
while i < N:
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(arr, n)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    i += 1
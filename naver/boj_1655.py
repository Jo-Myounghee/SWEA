import heapq, sys

N = int(input())
max_lst = []
min_lst = []
for i in range(N):
    n = int(sys.stdin.readline())
    if len(max_lst)-len(min_lst) <= 0:
        heapq.heappush(max_lst, (-n, n))
    else:
        heapq.heappush(min_lst, n)

    if max_lst and min_lst and max_lst[0][1] > min_lst[0]:
        maxtomin = heapq.heappop(max_lst)[1]
        mintomax = heapq.heappop(min_lst)
        heapq.heappush(min_lst, maxtomin)
        heapq.heappush(max_lst, (-mintomax, mintomax))

    print(max_lst[0][1])
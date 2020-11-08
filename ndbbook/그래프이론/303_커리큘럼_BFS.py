'''
inputs
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
outputs
10
20
14
18
17
'''

def bfs(n):
    total = 0
    q = pre_lectures[n]
    total += times[n]

    while q:
        i = q.pop(0)
        if pre_lectures[i]:
            q.insert(pre_lectures[i])
        else:
            total += times[i]
    return total

# BFS로 풀 수 있을 듯
N = int(input())
pre_lectures = [[] for _ in range(N+1)]
times = [0] * (N+1)
inputs = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    times[i] = inputs[i-1][0]
    j = 1
    while j < len(inputs[i-1]) and inputs[i-1][j] != -1:
        pre_lectures[i].append(inputs[i-1][j])
        j += 1

for i in range(1, N+1):
    print(bfs(i))

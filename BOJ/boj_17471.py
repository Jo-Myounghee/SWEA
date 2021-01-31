from collections import deque

def bfs(lst):
    if len(lst) == 1:
        return True
    global N
    visited = [0] * (N+1)
    visited[lst[0]+1] = 1
    q = deque(board[lst[0]+1])
    while q:
        if sum(visited) == len(lst):
            return True
        next_num = q.popleft()
        if visited[next_num] == 0 and next_num-1 in lst:
            visited[next_num] = 1
            q.extend(board[next_num])
    return False

N = int(input())
people = list(map(int, input().split()))
board = [[] for _ in range(N+1)]
ans = 1e9

for i in range(N):
    tmp = list(map(int, input().split()))
    board[i+1] = tmp[1:]

for i in range(1<<N):
    sum1, sum2 = 0, 0
    tmp1 = []
    tmp2 = []
    for j in range(len(people)):
        if i&(1<<j):
            tmp1.append(j)
            sum1 += people[j]
        else:
            tmp2.append(j)
            sum2 += people[j]

        if len(tmp1) == N or len(tmp2) == N or len(tmp1) + len(tmp2) != N:
            continue
        # 여기서 합 확인하고, 다 연결되어있는지 확인
        if abs(sum1 - sum2) < ans:
            # 다 연결되어 있는지 확인
            if bfs(tmp1) == True and bfs(tmp2) == True:
                ans = abs(sum1 - sum2)

if ans == 1e9:
    print(-1)
else:
    print(ans)
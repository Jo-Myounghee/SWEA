from collections import deque, defaultdict


def solution():
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))   # 건설하는데 걸리는 시간
    indegree = [0] * (N+1)   # 진입차수
    graph = defaultdict(list)
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    GOAL = int(input())
    # start 지점 찾기(최상단 노드)
    start = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            start.append(i)

    q = deque()
    for s in start:
        q.append(s)

    answer = times[:]

    while q:
        n = q.popleft()
        if n == GOAL:
            break
        answer.append(n)
        for i in graph[n]:
            answer[i] = max(answer[i], answer[n]+times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return answer[GOAL]


T = int(input())
for _ in range(T):
    print(solution())
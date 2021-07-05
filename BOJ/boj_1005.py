from collections import deque, defaultdict


def solution():
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))   # 건설하는데 걸리는 시간
    cnt_lst = [0] * (N+1)   # 부모 노드 갯수
    dct = defaultdict(list) # key: 부모, val: 자식
    for _ in range(K):
        x, y = map(int, input().split())
        dct[x].append(y)
        cnt_lst[y] += 1
    GOAL = int(input())
    # start 지점 찾기(최상단 노드)
    start = []
    for i in range(1, N+1):
        if cnt_lst[i] == 0:
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
        for i in dct[n]:
            answer[i] = max(answer[i], answer[n]+times[i])
            cnt_lst[i] -= 1
            if cnt_lst[i] == 0:
                q.append(i)
    return answer[GOAL]


T = int(input())
for _ in range(T):
    print(solution())
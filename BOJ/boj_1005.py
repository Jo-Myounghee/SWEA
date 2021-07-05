'''
1
4 3
5 5 5 5
1 2
1 3
2 3
4
'''

from collections import deque, defaultdict


def solution():
    answer = 0
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))   # 건설하는데 걸리는 시간
    print(times)
    cnt_lst = [0] * (N+1)   # 부모 노드 갯수
    dct = defaultdict(list) # key: 부모, val: 자식
    for _ in range(K):
        x, y = map(int, input().split())
        dct[x].append(y)
        cnt_lst[y] += 1
    GOAL = int(input())
    # start 지점 찾기(최상단 노드)
    for i in dct:
        if cnt_lst[i] == 0:
            start = i
    print(start, 'start')

    q = deque()
    for node in dct[start]:
        q.append((node, times[start]+times[node]))

    while cnt_lst[GOAL] > 0:
        n, v = q.popleft()
        cnt_lst[n] -= 1
        if n == GOAL:
            answer = max(v, answer)
        else:
            for node in dct[n]:
                q.append((node, v+times[node]))
    return answer


T = int(input())
for _ in range(T):
    print(solution(), 'answer')
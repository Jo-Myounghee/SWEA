# N 도시의 갯수, M 통로의 갯수, C 메시지를 보내고자 하는 도시

# X, Y, Z 도시X에서 도시Y까지 Z시간 소요

# 출력 : 도시 C에서 보낸 메시지를 받는 도시의 총 갯수, 총 걸리는시간

'''
input
3 2 1
1 2 4
1 3 2
output
2 4
'''
from collections import deque

def dijkstra(start):
    q = deque()
    q.append((0, start))
    distance[start] = 0
    while q:
        dist, now = q.popleft()
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((cost, i[0]))

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))
dijkstra(start)

count = 0

max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)

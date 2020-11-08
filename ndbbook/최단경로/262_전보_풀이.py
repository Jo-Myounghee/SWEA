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
import heapq
import sys

input = sys.stdin.readline()
INF = int(1e9)

# n 노드의 개수, m 간선의 개수, start 시작 노드
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 z라는 의미
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드의 갯수
count = 0

# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)

'''
inputs
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
def prim(V):
    total = 0
    curV = 1
    D = [0] * (V+1)
    u = [1]

    for i in range(1, V+1):
        D[i] = graph[1][i]
    while len(u) < V:
        minV = 1001
        for i in range(V+1):
            if i not in u:
                if minV > D[i]:
                    minV = D[i]
                    curV = i
        total += minV
        for i in range(V+1):
            if i not in u:
                if D[i] > graph[curV][i]:
                    D[i] = graph[curV][i]

        u.append(curV)
    return total

V, E = map(int, input().split())
graph = [[1001] * (V+1) for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A][B] = C
    graph[B][A] = C

print(prim(V))
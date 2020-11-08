def prim(V):
    total = 0
    curV = 1
    D = [0] * (V+1)
    u = [1]

    for i in range(V+1):
        D[i] = graph[1][i]
    while len(u) <= V:
        minV = 11
        for i in range(V+1):  # 가중치가 가장 작은 값 구하기 -> curV에 할당
            if i not in u:
                if minV > D[i]:
                    minV = D[i]
                    curV = i
        total += minV
        for i in range(V+1):  # curV을 기준으로 distance리스트를 바꾸자
            if i not in u:
                if D[i] > graph[curV][i]:
                    D[i] = graph[curV][i]

        u.append(curV)
    return total
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[11] * (V+1) for _ in range(V+1)]
    inputs = [list(map(int, input().split())) for _ in range(E)]
    for i in range(len(inputs)):
        v, e, val = inputs[i][0], inputs[i][1], inputs[i][2]
        graph[v][e] = val
        graph[e][v] = val

    print('#{} {}'.format(tc, prim(V)))
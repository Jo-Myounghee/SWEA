def DFS(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for dir in range(4):
            testX = x + dx[dir]
            testY = y + dy[dir]
            DFS(testX, testY)
        return True
    return False

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

result = 0
for y in range(n):
    for x in range(m):
        if DFS(x, y) == True:
            result += 1
print(result)

# test_case
# 4 5
# 00110
# 00011
# 11111
# 00000
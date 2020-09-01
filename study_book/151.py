n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

def DFS(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    return False

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
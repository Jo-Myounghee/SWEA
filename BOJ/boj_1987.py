R, C = map(int, input().split())
map = [list(map(str, input())) for _ in range(R)]

answer = 0
visited = [False] * 26
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(x, y, n):
    global answer
    answer = max(n, answer)
    for i in range(4):
        tx = x + dir[i][0]
        ty = y + dir[i][1]

        if tx < 0 or tx >= C or ty < 0 or ty >= R:
            continue

        if visited[ord(map[ty][tx])-ord('A')]:
            continue

        visited[ord(map[ty][tx]) - ord('A')] = True
        dfs(tx, ty, n+1)
        visited[ord(map[ty][tx]) - ord('A')] = False

visited[ord(map[0][0])-ord('A')] = True
dfs(0, 0, 1)
print(answer)


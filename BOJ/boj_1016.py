import math

MIN, MAX = map(int, input().split())
visited = [False] * (MAX + 1 - MIN)
cnt = 0

for i in range(2, int(math.sqrt(MAX))+1):
    t = 1
    test = (i**2) * t

    while test <= MAX:
        if test >= MIN and not visited[test]:
            visited[test-MIN] = True
            cnt += 1
        t += 1
        test = (i**2) * t

print(MAX-MIN+1-cnt)
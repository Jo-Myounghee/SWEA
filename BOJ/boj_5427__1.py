from collections import deque

def get_input():
    for i in range(h):
        row = input()
        area.append(row)
        for j in range(w):
            if row[j] == '*':
                fire_pos.append([i, j])
            elif row[j] == '@':
                person_pos.append([i, j])

def bfs(pos):
    q = deque(pos)
    rtn = dict()
    time = 0
    visited = [[False] * w for _ in range(h)]

    for i, j in pos:
        visited[i][j] = True

    while q:
        time += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for a in range(4):
                ni, nj = i + dir[a][0], j + dir[a][1]
                if 0 <= ni < h and 0 <= nj < w:
                    if area[ni][nj] != '#' and not visited[ni][nj]:
                        q.append([ni, nj])
                        visited[ni][nj] = True
                else:
                    rtn[(i, j)] = time
    return rtn

for _ in range(int(input())):
    w, h = map(int, input().split())
    dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    fire_pos = []
    person_pos = []
    area = []
    get_input()

    fire = bfs(fire_pos)
    person = bfs(person_pos)

    print(fire, 'fire')
    print(person, 'person')

    if not person:
        print('IMPOSSIBLE')
    else:
        for (i, j) in fire:
            try:
                if person[(i, j)] >= fire[(i, j)]:
                    person[(i, j)] = float('inf')
            except:
                person[(i, j)] = float('inf')
        min_val = min(person.values())
        print('IMPOSSIBLE' if min_val == float('inf') else min_val)

    print(fire, 'fire')
    print(person, 'person')
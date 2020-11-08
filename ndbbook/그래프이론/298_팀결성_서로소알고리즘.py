'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''

# 같은 팀 여부 확인
def parent_finds(n):
    if n != parents[n]:
        return parent_finds(parents[n])
    return parents[n]

# 팀 합치기
def union_team(a, b):
    a = parent_finds(a)
    b = parent_finds(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(N+1)]
parents = [0] * (N+1) # 부모 확인용

for i in range(N+1):
    parents[i] = i

for i in range(len(inputs)):
    F, a, b = inputs[i]
    if F:
        if parent_finds(a) != parent_finds(b):
            print('NO')
        else:
            print('YES')
    else:
        union_team(a, b)

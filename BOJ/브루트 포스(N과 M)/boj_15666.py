def perm(s, val):
    global groups
    if len(val) == M:
        groups.add(tuple(val))
        return
    for i in range(s, N):
        perm(i, val+[nums[i]])


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
groups = set()
perm(0, [])
for group in sorted(groups):
    print(*group)
def make_group(now, val):
    global answer
    if len(val) == M:
        answer.add(tuple(val))
        return
    for i in range(N):
        make_group(now, val + [nums[i]])


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = set()
make_group(0, [])
for group in sorted(answer):
    print(*group)
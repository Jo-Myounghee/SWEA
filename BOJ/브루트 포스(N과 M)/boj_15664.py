def make_group(start, val):
    global answer
    if len(val) == M:
        now = ' '.join(map(str, val))
        if now not in answer:
            answer.append(' '.join(map(str, val)))
        return
    for i in range(start, N):
        make_group(i+1, val + [nums[i]])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []
make_group(0, [])
for i in answer:
    print(i)
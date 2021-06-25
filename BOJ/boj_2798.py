def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    answer = 0

    def make_sum(start, cnt, val):
        nonlocal answer
        if cnt == 3:
            if val <= M:
                answer = max(answer, val)
            return

        for i in range(start, N):
            make_sum(i+1, cnt+1, val+nums[i])

    make_sum(0, 0, 0)
    print(answer)


solution()
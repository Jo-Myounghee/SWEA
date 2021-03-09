N = int(input())
nums = [1] * N
if N > 2:
    for i in range(2, N):
        nums[i] = nums[i-1] + nums[i-2]
    print(nums[N-1])
else:
    print(1)
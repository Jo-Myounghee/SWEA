'''
3 3 
1
4
6

2
'''
import sys
N, C = map(int, sys.stdin.readline().rstrip().split())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))
nums.sort()

start = 1
end = nums[-1] - nums[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    val = nums[0]
    cnt = 1
    for i in range(1, N):
        if nums[i] >= val + mid:
            val = nums[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
import sys
# sys.stdin = open('5input.txt', 'r')
sys.stdin = open('5input1.txt', 'r')

N, M = map(int, input().split())
nums = list(map(int, input().split()))

total_ans = (N * (N-1))//2
sub_ans = 0

nums.sort()
prev = 0
multi = []
for i in range(len(nums)):
    if prev != nums[i]:
        prev = nums[i]
    else:
        if not [prev, nums.count(prev)] in multi:
            multi.append([prev, nums.count(prev)])


for i in range(len(multi)):
    sub_ans += multi[i][1] * (multi[i][1]-1) // 2

print(total_ans - sub_ans)

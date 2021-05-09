'''
1. 뒤에서부터 x > y인 부분 찾기
2. y_idx 이후부터 끝까지 중 : x보다는 작으면서 가장 큰 값(max)을 찾음
3. max와 x를 swap
4. max_idx 이후부터 맨 마지막까지 역 sort

3
3 1 2
-> 2 3 1
3
2 1 3
-> 1 3 2
'''
def find():
    global nums
    for i in range(len(nums)-1, 0, -1):
        x, y = nums[i-1], nums[i]
        if x > y:
            find_nums = sorted(nums[i:], reverse=True)
            for j in find_nums:
                if j < x:
                    max_idx = nums.index(j)
                    break
            nums[i-1], nums[max_idx] = nums[max_idx], nums[i-1]
            nums[i:] = sorted(nums[i:], key=lambda x: -x)
            return

N = int(input())
nums = list(map(int, input().split()))
if nums == sorted(nums):
    print(-1)
else:
    find()
    print(*nums, sep=" ")
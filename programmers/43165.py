def cal(idx, val):
    global nums, answer, t
    if idx == len(nums):
        if val == t:
            answer += 1
        return
    cal(idx+1, val+nums[idx])
    cal(idx+1, val-nums[idx])

def solution(numbers, target):
    global nums, answer, t
    nums = numbers
    t = target
    answer = 0
    cal(0, 0)
    return answer
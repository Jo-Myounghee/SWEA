def func(n, temp):
    global N, nums, signs, max_val, min_val

    if n == N:
        max_val = max(temp, max_val)
        min_val = min(temp, min_val)
        return

    for i in range(4):
        if signs[i] > 0:
            signs[i] -= 1
            if i == 0:
                func(n+1, temp+nums[n])
            if i == 1:
                func(n+1, temp-nums[n])
            if i == 2:
                func(n+1, temp*nums[n])
            if i == 3:
                if temp < 0:
                    temp_ans = (-temp) // nums[n]
                    temp_ans = -temp_ans
                else:
                    temp_ans = temp // nums[n]
                func(n+1, temp_ans)
            signs[i] += 1

N = int(input())
nums = list(map(int, input().split()))
signs = list(map(int, input().split()))
max_val, min_val = -1e9, 1e9
func(1, nums[0])
print(max_val, min_val, sep="\n")
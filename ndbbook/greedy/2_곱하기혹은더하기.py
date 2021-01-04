import sys
# sys.stdin = open('2input.txt', 'r')
sys.stdin = open('2input1.txt', 'r')

def DP(temp, k):
    global ans
    if temp > ans:
        ans = temp
    if k == len(nums)-1:
        return
    else:
        DP(temp*nums[k+1], k+1)
        DP(temp+nums[k+1], k+1)

# DP 문제
nums = list(map(int, input()))
ans = 0
DP(nums[0], 0)
print(ans)


# 해결법 ----------------------------------------------
# data = input()
#
# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])
#
# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)
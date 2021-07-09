def make_sum_lst():
    sum_lst = [inputs[0]]
    for i in range(1, len(inputs)):
        sum_lst.append(sum_lst[-1]+inputs[i])
    return sum_lst


def solution():
    s, e = map(int, input().split())
    return nums[e-1] - nums[s-1] + inputs[s-1]


N, M = map(int, input().split())
inputs = list(map(int, input().split()))
nums = make_sum_lst()
for _ in range(M):
    print(solution())
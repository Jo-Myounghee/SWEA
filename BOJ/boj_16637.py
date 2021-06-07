def divide_num_operator(string):
    global nums, operators
    for i in string:
        if i.isdigit():
            nums.append(int(i))
        else:
            operators.append(i)


def calc(n1, n2, operator):
    if operator == '*':
        return n1 * n2
    elif operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2


def dfs(idx, ret):
    global answer
    if idx >= len(operators):
        answer = max(answer, ret)
        return

    dfs(idx+1, calc(ret, nums[idx+1], operators[idx]))

    if idx + 1 < len(operators):
        dfs(idx+2, calc(ret, calc(nums[idx+1], nums[idx+2], operators[idx+1]), operators[idx]))


def solution(arr):
    divide_num_operator(arr)
    dfs(0, nums[0])


N = int(input())
inputs = list(input())
answer = -1e9
nums, operators = [], []
solution(inputs)
print(answer)
